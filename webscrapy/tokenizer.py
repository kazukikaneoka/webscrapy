import re

class Tokenizer(object):

    def __init__(self):
        pass

    def tokenize(self, html_tag):
        html_tag = html_tag.strip()
        if not re.match(r'^<(.+?)>$', html_tag):
            raise RuntimeError("ERROR: Invalid HTML_TAG")
        tokens = re.split(r'\s+', html_tag[1:-1])
        d = {}
        for i, token in enumerate(tokens):
            if i == 0:
                d['name'] = token
            elif 'class' in token:
                self.add_token(token, d, 'class')
            elif 'rel' in token:
                self.add_token(token, d, 'rel')
            elif 'rev' in token:
                self.add_token(token, d, 'rev')
            elif 'accept-charset' in token:
                self.add_token(token, d, 'accept-charset')
            elif 'headers' in token:
                self.add_token(token, d, 'headers')
            elif 'accesskey' in token:
                self.add_token(token, d, 'accesskey')
            else:
                m = re.search(r'^(.+?)="(.+?)"', token)
                d[m.group(1)] = m.group(2)
        return d

    def add_token(self, token, d, key):
        if key not in d:
            d[key] = []
        d[key].append(re.search(r'"(.+?)"', token).group(1))
