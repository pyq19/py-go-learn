import requests
from bs4 import BeautifulSoup

from setting import URLS, HEADERS


class Spider(object):
    def __init__(self, url, headers=HEADERS[0]):
        self.url = url
        self.headers = headers

    @property
    def urls(self):
        html = requests.get(self.url, headers=self.headers).text
        soup = BeautifulSoup(html, 'html.parser')
        def _get_urls_from(html):
            # 解析所有子url
            _urls = []
            for link in soup.find_all('a'):
                _urls.append(link.get('href'))
            return _urls
        return _get_urls_from(html)

    def data(self, urls):
        print(urls)
        def _get_data_from(u):
            # 从传入的url 解析数据
            _res = 'wawawawa'
            return _res 
        for u in urls:
            return _get_data_from(u)


def run():
    spider = Spider(URLS['cqgov'] + 'today/news/default_1.shtml')
    for u in spider.urls:
        print(spider.data(u))
    
        
if __name__ == '__main__':
    run()
