#coding:utf8

import requests
from setting import URLS, HEADERS 

#def main2():
#    print(requests.get(URLS['cqgov'], headers=HEADERS[0], timeout=30).text)

class Spider(object):
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = HEADERS[0] if headers is None else headers
    
    @property
    def urls(self, pages=5):
        print(self.base_url)
        print(self.headers)
        html = requests.get(self.base_url, headers=self.headers).text
        print(html)

        urls = ['aaa', 'bbb', 'ccc']
        for url in urls:
            yield url

    def parse_html(self, url):
        print(url)

def main(url):
    s = Spider(url)
    for u in s.urls:
        s.parse_html(u)

if __name__ == '__main__':
    #main(URLS['cqgov'] + 'today/news/default_1.shtml')
    main2()
