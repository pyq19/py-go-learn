# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import datetime, re

import scrapy
from scrapy.loader import ItemLoader # 定义自己的ItemLoader，重载这个类
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_jobbole(value):
    return value + '-add_jobbole'


def date_convert(value):
    try:
        create_time = datetime.datetime.strptime(value, '%Y/%m/%d').date()
    except Exception as e:
        create_time = datetime.datetime.now().date()
    return create_time


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


def remove_comment_tags(value):
    # 去掉tag中提取的评论
    if '评论' in value:
        return ''
    else:
        return value


def return_value(value):
    return value


class ArticleItemLoader(ItemLoader):
    # 自定义itemloader，就不用每个item的属性加上scrapy.Field(output_processor=TakeFirst())
    # 需要在jobbole.py里用自定义的ArticleItemLoader
    default_output_processor = TakeFirst()
    # TakeFirst之后，jobbole.py里article_item返回的不再是列表list


class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field(
        # 对传到title的值进行预处理
        # input_processor = MapCompose(add_jobbole)
        # input_processor = MapCompose(lambda x: x + '-jobbole', add_jobbole)
    )
    create_time = scrapy.Field(
        input_processor = MapCompose(date_convert) # ,
        # output_processor = TakeFirst() # 只取第一个
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field( # !!!!! 图片地址str在pipeline下载会抛异常（原来是list）
        output_processor=MapCompose(return_value)
    ) 
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(',') # !!!!!
    )
    content = scrapy.Field()

