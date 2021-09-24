# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import re

class HgcImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for img_url in item['img_url']:
            print(img_url)
            yield Request(img_url,meta={
                'flie_name':item['flie_name']
            })

    def file_path(self, request, response=None, info=None, *, item=None):




        # 提取url前面名称作为图片名。
        image_guid = request.url.split('/')[-1]
        print(image_guid)
        # 接收上面meta传递过来的图片名称
        name = request.meta['flie_name']
        # 过滤windows字符串，不经过这么一个步骤，会有乱码或无法下载
        name = re.sub(r'[？\\*|“<>:/]', '', name)
        filename = u'{}/{}'.format(name, image_guid)
        return filename












