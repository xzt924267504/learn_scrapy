
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import re
import pymysql

class T66YPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for img_url in item['img_url']:
            yield Request(img_url,meta={
                "flie_name":item['flie_name']
            })

    def file_path(self, request, response=None, info=None, *, item=None):
        #
        # file_path = ''.join(re.findall('https://x6img.com/i/2021/06/04/(.*?.jpg)',request.url))
        # return f'{file_path}'

        # 提取url前面名称作为图片名。
        image_guid = request.url.split('/')[-1]
        # 接收上面meta传递过来的图片名称
        name = request.meta['flie_name']
        # 过滤windows字符串，不经过这么一个步骤，会有乱码或无法下载
        name = re.sub(r'[？\\*|“<>:/]', '', name)
        filename = u'{}/{}'.format(name, image_guid)
        return filename






# class MySQLPipline(object):
#
#     def __init__(self):
#         # 连接数据库
#         self.connect = pymysql.connect(
#             host='127.0.0.1',  # 数据库地址
#             port=3306,  # 数据库端口
#             db='t66y',  # 数据库名
#             user='root',  # 数据库用户名
#             passwd='123456',  # 数据库密码
#             charset='utf8',  # 编码方式
#             use_unicode=True)
#
#         # 通过cursor执行增删查改
#         self.cursor = self.connect.cursor()
#     def process_item(self,item,spider):
#         for i in item['img_url']:
#             i = i.split('/')[-1]
#
#             # '''insert into t66y(folder,file_name)value ({},{})'''.format(item['flie_name'],i)
#             sql = """insert into t66y(folder,file_name)value (%s, %s)""",(item['flie_name'], i)
#             print('__________________________')
#             print(sql)
#             print('__________________________')
#             self.cursor.execute(sql)
#
#             # 提交sql语句
#             self.connect.commit()
#         return item  # 必须实现返回