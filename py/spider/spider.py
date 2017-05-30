from itertools import chain
import time

import requests
from lxml import html


URL = 'http://www.cq.gov.cn/today/news/'
HOST = 'http://www.cq.gov.cn/'
HEADERS = [
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
        'Host': 'www.cq.gov.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,vi;q=0.2',
        'X-Requested-With':'XMLHttpRequest', # !!!
    },
]


class Result(object):
    
    def __init__(self, *args, **kwargs):
        try:
            self._url = kwargs.get('link', None)
            self._title = kwargs.get('title', None)
            self._date = kwargs.get('date', None)
            self._content = kwargs.get('content', None)
        except AttributeError as err:
            print('ERROR!! -> %s' % str(err))

    def save(self):
        print('TODO SAVE {title}'.format(title=self._title))

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def date(self):
        return self._date

    @property
    def content(self):
        return self._content
        
    def __str__(self):
        # return '''title-> {title}url-> {url}date-> {date}content-> {content}
        #        '''.format(title=self._title, url=self._url, date=self._date, content=self._content[:10]) 
        return 'title -> {title}, url -> {url}'.format(title=self._title, url=self._url)

    __repr__ = __str__


class Spider(object):

    def __init__(self, url, *arg, **kwargs):
        self.url = url
        self.headers = kwargs.get('headers', None)
        self.urls = []

    def _get_html(self, *args, **kwargs):
        url = kwargs.get('link', None)
        headers = kwargs.get('headers', None)
        # if not url.endswith('/'):
        #     raise ValueError('url must end with /')
        if url is None:
            print('no headers or url')
            req = requests.get(self.url)
            req.encoding = 'utf-8'
            text = req.text
            self.tree = html.fromstring(text)
            return text
        # print('get HTML from url ->', url)
        req = requests.get(url, headers=self.headers)
        req.encoding = 'utf-8'
        text = req.text
        self.tree = html.fromstring(text)
        return text

    def _get_urls(self, html):
        names = self.tree.xpath('/html/body/div[2]/div[2]/ul/li[*]/a/text()')
        links = self.tree.xpath('/html/body/div[2]/div[2]/ul/li[*]/a//@href')
        tem = dict(zip(names, links))
        for n, l in tem.items():
            self.urls.append({'title': n, 'link': l})

    def _get_contents(self, urls):
        def _one_page(link):
            # print('get CONTENT from ->', link)
            date, content = 'ddd', 'ccc'  # !!!
            # html = self._get_html(**{'link': link, 'headers': HEADERS[0]})
            html = self._get_html(**{'link': link})
            # with open('tmp_articl_%s.html' % time.time(), 'w') as f:
            #     f.write(html)

            return {'date': date, 'content': content}

        for url_dic in urls:
            _link = url_dic['link']
            if _link.startswith('/'):
                url_dic['link'] = HOST + _link[1:]

        results = []
        for url_dic in urls:
            page_dic = _one_page(url_dic['link'])
            # results.append(dict(page_dict, **url_dic))
            res = dict(chain(page_dic.items(), url_dic.items()))
            results.append(res)

        return results

    def _save(self, reslist):
        if not isinstance(reslist, list):
            print('ERR reslist, _safe fail')
        for res in reslist:
            res.save()

    def run(self):
        html = self._get_html()
        print('main html done')
        self._get_urls(html)
        print('get urls from main url<{url}> done.'.format(url=self.url))
        contents = self._get_contents(self.urls)
        results = []
        for con in contents:
            res = Result(**con)
            results.append(res)
        print('get results from urls done..')
        self._save(results)
        print('save done')


if __name__ == '__main__':
    spi = Spider(url=URL)
    spi.run()
