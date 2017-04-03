from scrapy.cmdline import execute

import sys, os

print(os.path.dirname(os.path.abspath(__file__))) # /Users/Mccree/p/scrapy/ArticleSpider
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'jobbole'])
