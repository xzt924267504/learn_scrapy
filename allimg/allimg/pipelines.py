# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import re
class AllimgPipeline(ImagesPipeline):
    def open_spider(self, spider):
        # 1. 建立数据库的连接
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='test',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()


    def get_media_requests(self, item, info):
        for author_img_url in item['author_img_url']:
            yield Request(author_img_url,meta={'author_img_url':item['author_img_url']})

    def file_path(self, request, response=None, info=None, *, item=None):

        '''自定义图片保存路径,以图片的url保存,重写前是图片的url经过MD5编码后存储'''
        file_path = ''.join(re.findall('http://lab.scrapyd.cn/usr/uploads/(.*?.jpg)',request.url))
        print(file_path)
        return f'{file_path}'

    pass

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
















