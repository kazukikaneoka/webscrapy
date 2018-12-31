import argparse
import datetime
import scraper
import sys
import tokenizer
from collections import namedtuple

class Webscrapy(object):

    def __init__(self):
        pass

    def run(self):
        
        # parse command line arguments
        parser, arguments = self.parse_arguments()
        if len(sys.argv) == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
            parser.print_help()
            return
        elif len(sys.argv) < 3:
            raise RuntimeError("ERROR: URL and HTML_TAG are required")
        config = self.config(arguments)
        url, tag = sys.argv[1], sys.argv[2]
        print("Web Scraping with url={} tag={} next={} max={}"\
            .format(url, tag, config.next, config.max if config.max > 0 else 'infinite'))

        # tokenize HTML_TAG
        t = tokenizer.Tokenizer()
        tag_info = t.tokenize(tag)

        # scrape HTML_TAG in URL
        s = scraper.Scraper()
        crawled_data = s.crawl(url, tag_info, config.next, config.max)

        # print out data
        for data in crawled_data:
            print(data)

    def config(self, arguments):
        d = arguments.__dict__
        keys = d.keys()
        args = [d[key] for key in keys]
        config = namedtuple('Config', keys)
        return config(*args)

    def parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-n', '--next', action='store_true',
            help="Scrape next urls (next urls = urls which has same prefix with URL")
        parser.add_argument('-m', '--max', type=int, default=0,
            help="Max number of urls to scrape when using -n (max number of urls = = infinite if not using -m)")
        arguments = parser.parse_args(sys.argv[3:])
        return parser, arguments

if __name__ == '__main__':
    obj = Webscrapy()
    obj.run()
