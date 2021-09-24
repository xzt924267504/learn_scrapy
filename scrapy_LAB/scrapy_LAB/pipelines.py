# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from items import ScrapyLabItem
import pymysql
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.pipelines.files import FilesPipeline
import re
import scrapy

class ScrapyLabPipeline(ImagesPipeline):



    def get_media_requests(self, item, info):

        """循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield"""
        for image_url in item['author_img_url']:

            yield Request(image_url,meta={'author_img_url':item['author_img_url']})


        # 如果要选择自己的文件名输出格式, 必须重写FilesPipeline类的file_path方法
    def file_path(self, request, response=None, info=None, *, item=None):

        '''自定义图片保存路径,以图片的url保存,重写前是图片的url经过MD5编码后存储'''
        file_path = ''.join(re.findall('http://lab.scrapyd.cn/usr/uploads/(.*?.jpg)',request.url))


        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='test',
            charset='utf8'
        )

        self.cursor = self.connect.cursor()
        insert_sql = "INSERT INTO demo VALUES ('{}');".format(file_path)
        # print(insert_sql)
        self.cursor.execute(insert_sql)
        self.connect.commit()

        print(file_path)
        return f'{file_path}'

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


