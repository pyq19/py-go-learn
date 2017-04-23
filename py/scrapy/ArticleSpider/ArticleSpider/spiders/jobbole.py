# -*- coding: utf-8 -*-
import re
import scrapy
import datetime

from scrapy.http import Request # 将这个Request 对象交给scrapy
from urllib import parse # 对url 进行拼接yield Request(url=parse.urljoin(response.url, post_url), callback=..)
from scrapy.loader import ItemLoader

from ArticleSpider.items import JobBoleArticleItem, ArticleItemLoader

from ArticleSpider.utils.common import get_md5

class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']
#    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        """
        1 获取文章列表页中的文章url并交给scrapy下载后，进行解析
        2 获取下一页的URL并交给scrapy进行下载，下载完成后交给parse函数循环第一步
        """

        # re_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1')
        # re_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()') # 加text()!
        # title = response.xpath('//div[@class='entry-header']/h1/text()') # title 是个selector 方法, 可以进一步调用
        # title.extract() # ['....']
        # title.extract()[1] # '....'.strip().replace('aaa', '')


        # 解析列表页中的所有文章url并交给srapy下载后，进行解析
#        post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url}, callback=self.parse_detail)
            # Request(url=post_url, callback=self.parse_detail)
            # >>> post_urls = ['/aa','/bb']
            # >>> for a in post_urls:
            # ...     url=parse.urljoin(response.url, a)
            # ...     print(url)
            # http://blog.jobbole.com/aa
            # http://blog.jobbole.com/bb
            # response.url -> 'http://blog.jobbole.com/all-posts/'
            # >>> post_urls = ['http://blog.jobbole.com/110574/','http://blog.jobbole.com/110557/']
            # >>> for a in post_urls:
            # ...     url=parse.urljoin(response.url, a)
            # ...     print(url)
            # ...
            # http://blog.jobbole.com/110574/
            # http://blog.jobbole.com/110557/
            # yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": }, callback=self.parse_detail)

        # 提取下一页并交给scrapy下载
#       >>> response.css(".next.page-numbers").extract_first("")
#       '<a class="next page-numbers" href="http://blog.jobbole.com/all-posts/page/2/">下一页 »</a>'
#       >>> response.css(".next.page-numbers::attr(href)").extract_first("")
#       'http://blog.jobbole.com/all-posts/page/2/'
        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

         
    def parse_detail(self, response):
        article_item = JobBoleArticleItem()

        
        # 提取文章的具体字段

# #        re_selector = response.xpath('/html/body/div[3]/div[3]/div[1]/div[1]/h1')  # 要把第一个3改成1
# #        re_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()')
#         re_selector = response.xpath('//div[@class="entry-header"]/h1/text()')
# #        response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace('·', '').strip() # 2017/02/18
#         ct_selector = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()")
# #        response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract() # ['2']
#         title = re_selector.extract()[0]
#         create_time = ct_selector.extract()[0].strip().replace('·', '').strip()
#         praise_nums = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])
# #        response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0] # ' 22 收藏'
#         fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
#         match_re = re.match(".*?(\d+).*", fav_nums)
#         if match_re:
#             fav_nums = match_re.group(1)
# 
# #        response.xpath("//a[@href='#article-comment']/span/text()").extract()[0] # ' 6 评论'
#         comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]        
#         match_re = re.match(".*?(\d+).*", comment_nums)
#         if match_re:
#             comment_nums = match_re.group(1)
#         content = response.xpath("//div[@class='entry']").extract()[0]
# 
#         create_time = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace('·', '').strip()
#         
# #        response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract() # ['职场', ' 6 评论 ', '面试']
#         tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()  
#         tag_list = [element for element in tag_list if not element.strip().endswith('评论')]
#         tags = ','.join(tag_list) # '职场, 6 评论 ,面试'
#         print('xpath------>', title, create_time, praise_nums, fav_nums, comment_nums, tags)

        # 通过CSS选择器提取字段
#        front_image_url = response.meta.get('front_image_url', '') # 文章封面图
#        title = response.css(".entry-header h1::text").extract_first("").strip()
#        create_time = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace('·', '').strip()
#        praise_nums = response.css(".vote-post-up h10::text").extract()[0]
#        fav_nums = response.css("span.bookmark-btn::text").extract()[0]
#        match_re = re.match(".*?(\d+).*", fav_nums)
#        if match_re:
#            fav_nums = int(match_re.group(1))
#        else:
#            fav_nums = 0
#        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
#        match_re = re.match(".*?(\d+).*", comment_nums)
#        if match_re:
#            comment_nums = int(match_re.group(1))
#        else:
#            comment_nums = 0
#        content = response.css("div.entry").extract()[0]
#        tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
#        tag_list = [element for element in tag_list if not element.strip().endswith('评论')]
#        tags = ','.join(tag_list)
##        front_image_path = response.css().extract() # !!!
#        print('css------>', title, create_time, praise_nums, fav_nums, comment_nums, tags)
#
##        article_time 在函数第一行article_item = JobBoleArticleItem()
#        article_item['url_object_id'] = get_md5(response.url)
#        article_item['title'] = title
#        article_item['url'] = response.url
#        try:
#            create_date = datetime.datetime.strptime(create_date, '%Y/%m/%d').date() # !!!!!
#        except Exception as e:
#            create_time = datetime.datetime.now().date()
#        article_item['create_time'] = create_time 
#        article_item['front_image_url'] = [front_image_url] # !!!!
#        article_item['praise_nums'] = int(praise_nums)
#        article_item['front_image_path'] = '......'
#        article_item['fav_nums'] = int(fav_nums)
#        article_item['comment_nums'] = int(comment_nums) 
#        article_item['tags'] = tags  
#        article_item['content'] = content

        
        # from scrapy.loader import ItemLoader
        # !!!!! 通过ItemLoader加载item
        # item_loader.add_xpath()
        # item_loader = ItemLoader(item=JobBoleArticleItem(), response=response)
        # 这里的ItemLoader换成自定义的ArticleItemLoader，要从ArticleSpider/items.py里导入
        front_image_url = response.meta.get('front_image_url', '') # 文章封面图
        item_loader = ArticleItemLoader(item=JobBoleArticleItem(), response=response)
        item_loader.add_css('title', '.entry-header h1::text') # title 对应的提取样式
        item_loader.add_value('url', response.url)
        item_loader.add_value('url_object_id', get_md5(response.url))
        item_loader.add_css('create_time', 'p.entry-meta-hide-on-mobile::text')
        item_loader.add_value('front_image_url', [front_image_url])
        item_loader.add_css('praise_nums', '.vote-post-up h10::text')
        item_loader.add_css('comment_nums', "a[href='#article-comment'] span::text")
        item_loader.add_css('fav_nums', 'span.bookmark-btn::text')
        item_loader.add_css('tags', 'p.entry-meta-hide-on-mobile a::text')
        item_loader.add_css('content', 'div.entry')

        article_item = item_loader.load_item() # 调用load_item() 才会应用前面的规则解析生成item 对象
        print(article_item, '***^^^' * 30)
        yield article_item # 调用yield之后会传递到pipelines.py
