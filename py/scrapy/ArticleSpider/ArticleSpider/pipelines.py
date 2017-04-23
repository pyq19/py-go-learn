# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 在setting.py 中ITEM_PIPELINES = {'ArticleSpider.pipelines.ArticleSpiderPipeline':300,}  300表示处理顺序，越小越早
#                                   'scrapy.pipelines.images.ImagesPipeline':1,    配置这个pipeline 之后就可以下载图片
                                    # 下载图片还要配置IMAGES_URLS_FIELD 详见setting.py
# 就可以接受jobbole.py 传递过来的item

import codecs # ！！！避免编码问题？！ # 用codecs 可以避免很多编码问题
import json

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter # !!! scrapy 提供的写入json 文件机制，可以将item导出成各种类型的文件
from twisted.enterprise import adbapi # 将mysqldb操作变成异步

import MySQLdb # pip install mysqlclient
import MySQLdb.cursors

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        print('in pipline !!', '*' * 30)
        return item


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 将item 转换成字符串
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'   # 第二个参数重要，直接把unicode 编码写入文件中,中文显示正常
        self.file.write(lines)
        return item # 把item 返回去给下个pipeline 处理

    def spider_closed(self, spider): # 信号量？？
        self.file.close() # 关闭文件 


# class JsonExporterPipeline(object):
#     # 调用scrapy 提供的json export 导出json 文件
#     def __init__(self):
#         self.file = open('articleexport.json', 'wb')
#         self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
#         self.exporter.start_exporting()
#     下面有完整的类


class MySQLPipeline(object):
    def __init__(self):
        print('mysqlpipeline init....', '*' * 30)
        self.conn = MySQLdb.connect('localhost', 'root', 'forever367', 'scrapy', charset='utf8', use_unicode=True) # !!!
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
#         insert_sql = """
#             insert into jobbole_article(title, url, url_object_id, front_image_url, front_image_path, comment_nums, fav_nums, tags, content, praise_nums, create_time)
#             values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         self.cursor.execute(insert_sql, (item['title'], item['url'], item['url_object_id'], item['front_image_url'], item['front_image_path'], item['comment_nums'], item['fav_nums'], item['tags'], item['content'], item['praise_nums'], item['create_time']))
#         self.conn.commit() # !!! 不再是cursor操作
        insert_sql = 'insert into jobbole_article(title, url, url_object_id, comment_nums, fav_nums, content, praise_nums) values(%s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(insert_sql, (item['title'], item['url'], item['url_object_id'], item['comment_nums'], item['fav_nums'], item['content'], item['praise_nums']))
        self.conn.commit()
        return item


class MySQLTwistedPipeline(object):
    # MySQL异步插入
    def __init__(self, dbpool):
        self.dbpool = dbpool

    # from_settings 这个方法会被scrapy调用
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings['MYSQL_HOST'],
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWORD'],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparms) #!!!!!!! 将参数变成可变化参数
        # dbpool = adbapi.ConnectionPool(host=..., db=...)

        return cls(dbpool) # 实例化对象

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item) # 调用dbpool
        query.addErrback(self.handle_error)# 处理异常

    def handle_error(self, failure):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        insert_sql = 'insert into jobbole_article(title, url, url_object_id, comment_nums, fav_nums, content, praise_nums) values(%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(insert_sql, (item['title'], item['url'], item['url_object_id'], item['comment_nums'], item['fav_nums'], item['content'], item['praise_nums']))
 

class JsonExporterPipeline(object):
    # 调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file = open('article-export.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):   # 处理信号信号量
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


# from scraoy.pipelines.images import ImagesPipeline
# 只处理图片，可以在setting.py 中设置过滤大小等
# IMAGES_MIN_HEIGHT = 100
# IMAGES_MIN_WIDTH = 100 # 图片最小宽高
# 定义了这个pipeline之后就可以替换pipelines.py 里面的'scrapy.pipelines.images.ImagesPipeline': 1,
class ArticleImagePipeline(ImagesPipeline):
    # 获取到图片实际下载地址，路径存在results 里面
    def item_completed(self, results, item, info):
        print('in item_completed() !!', '*' * 30)
        if 'front_image_url' in item:
            for ok, value in results:
                image_file_path = value['path']
            item['front_image_path'] = image_file_path
        return item # 把item 返回去让下一个pipeline 处理（根据顺序）
