import re
import requests
# import codecs
import unittest
from io import StringIO

# from bs4 import BeautifulSoup
# from lxml import etree
from lxml import html


class TestSpider(unittest.TestCase):
    
    def setUp(self):
        try:
            f = open('text.html', 'r')
            text = f.read()
            f.close()

            f = open('article.html', 'r')
            article = f.read()
            f.close()
        except:
            text = '<title>error</title>'
        self.text = text
        # self.soup = BeautifulSoup(text, 'html.parser')
        # self.tree = etree.parse(StringIO(text))
        self.tree = html.fromstring(text)
        self.article = article
        self.urls = []

    def tearDown(self):
        pass

    # def test__get_html_to_file(self):
    #     req = requests.get('http://www.cq.gov.cn/today/news/default_1.shtml')
    #     req.encoding = 'utf-8'
    #     html = req.text
    #     # with open('text.html', 'w') as f:
    #     #     f.write(html)
    #     # file = codecs.open('text.html', 'w', 'utf8')
    #     # file.write(html)
    #     # file.close()
    
    # def test__get_urls_from_text(self):
    #     self.assertEqual(self.soup.title.get_text(), '今日重庆_重庆市政府网')

    # def test__get_all_urls(self):
    #     # print(self.soup.find_all(attrs={'class':'list'}))
    #     # for link in self.soup.find_all(attrs={'class':'list'}):
    #     #     print(link.get('href'))
    #     for tag in self.soup.find_all(attrs={'class':'list'}):
    #         # print(type(tag)) # <class 'bs4.element.Tag'>
    #         # print(tag.contents)
    #         for cont in tag.contents:
    #             print('-' * 20)
    #             print('*' * 20)
    #             print(type(cont))
    #             print(cont)
    #             reg = '<a href="(.*?)">.*?</a>'
    #             # print(re.search(reg, cont).group(0))

    def test__get_html_from_url(self):
        pass

    def test__get_all_urls(self):
        """[{'title':'xxx', 'link':'http...'},{...},...]"""
        _names, _links = [], []
        for name in self.tree.xpath('/html/body/div[2]/div[2]/ul/li[*]/a/text()'):
            _names.append(name)
        for link in self.tree.xpath('/html/body/div[2]/div[2]/ul/li[*]/a//@href'):
            _links.append(link)
        tem = dict(zip(_names, _links))
        for n, l in tem.items():
            self.urls.append({'title': n, 'link': l})
        
    # def test__save_html_to_file(self):
    #     req = requests.get('http://www.cq.gov.cn/today/news/2017/5/5/1500624.shtml')
    #     req.encoding = 'utf-8'
    #     text = req.text
    #     with open('article.html', 'w') as f:
    #         f.write(text)

    def test__get_complete_url(self):
        """ res = 'http://cq.gov.cn/today/22.shtml' """
        ts = [{'link': '/today/0.shtml', 'title': 'TTT'},\
          {'link': '/today/22.shtml', 'title': '重庆'}]
        host = 'http://cq.gov.cn/'
        for dic in ts:
            _link = dic['link']
            if _link.startswith('/'):
                dic['link'] = host + _link[1:]

    def test__get_article_detail(self):
        article_tree = html.fromstring(self.article)
        # title = article_tree.xpath(
        content = ''
        time = ''

    def test__save_to_sqlite(self):
        pass

    def test__save_to_mongodb(self):
        pass

    def test__save_to_redis(self):
        pass


if __name__ == '__main__':
    unittest.main()
