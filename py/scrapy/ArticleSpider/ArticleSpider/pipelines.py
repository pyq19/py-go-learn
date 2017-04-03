# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs # ！！！避免编码问题？！
import json

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter # !!!
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
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'   # 第二个参数重要
        self.file.write(lines)
        return item

    def spider_closed(self, spider): # 信号量？？
        self.file.close()


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
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparms) #!!!!!!!
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步
        query = self.dbpool.runInteraction(self.do_insert, item)
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


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        print('in item_completed() !!', '*' * 30)
        if 'front_image_url' in item:
            for ok, value in results:
                image_file_path = value['path']
            item['front_image_path'] = image_file_path
        return item
