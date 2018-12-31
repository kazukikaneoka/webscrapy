import re
import requests
from bs4 import BeautifulSoup
from collections import deque

class Scraper(object):

    def __init__(self):
        pass

    def crawl(self, url, tag_info, check_next, max_urls):
        crawled_data = self.bfs(url, tag_info, check_next, max_urls)
        return crawled_data

    def bfs(self, url, tag_info, check_next, max_urls):
        crawled_data = []
        urls = deque([url])
        visited_urls = set()

        while urls:
            current_url = urls.popleft()
            try:
                response = requests.get(current_url)
            except requests.RequestException as e:
                return dict(error=e.message)
            content = response.content
            soup = BeautifulSoup(content, 'html.parser')
            if len(tag_info) == 1:
                for tag in soup.find_all(lambda tag: tag.name == tag_info['name']):
                   crawled_data.append(tag.string)
            elif len(tag_info) > 1:
                for tag in soup.find_all(lambda tag: tag.name == tag_info['name'] and tag.get(key) == tag_info[key] for key in tag_info.keys()):
                    crawled_data.append(tag.string)
            visited_urls.add(current_url)
            if check_next and max_urls <= 0:
                urls = self.next_urls(soup, url, urls, visited_urls)
            elif check_next and len(visited_urls) < max_urls:
                urls = self.next_urls(soup, url, urls, visited_urls)
            else:
                break
        return crawled_data

    def next_urls(self, soup, prefix_url, urls, visited_urls):
        m = re.match(r'(.*?)(\.jp|\.com)(.*)', prefix_url)
        domain = m.group(1) + m.group(2)
        partial_path = m.group(3)
        for tag in soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') and re.search(partial_path, tag['href'])):
            next_url = tag['href'] if tag['href'] in domain else domain + tag['href']
            if next_url not in visited_urls and next_url.startswith(prefix_url) and next_url not in urls:
                urls.append(next_url)
        return urls
