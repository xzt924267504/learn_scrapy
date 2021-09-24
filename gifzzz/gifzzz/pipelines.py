
import pymysql
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import re

class GifzzzPipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        for img_url in item['img_url']:
            yield Request(img_url,meta={
                "flie_name":item['flie_name']
            })


    def file_path(self, request, response=None, info=None, *, item=None):
        self.con = pymysql.connect(
            host='127.0.0.1',  #服务器IP
            port=3306,  # 服务器端口号:不是字符串不需要加引号。
            user='root',
            password='123456',
            db='gifzzz',
            charset='utf8')
        # 得到一个可以执行SQL语句的光标对象
        self.cur = self.con.cursor()  # 执行完毕返回的结果集默认以元组显示

        # 提取url前面名称作为图片名。
        image_guid = request.url.split('/')[-1]
        # 接收上面meta传递过来的图片名称
        name = request.meta['flie_name']
        # 过滤windows字符串，不经过这么一个步骤，会有乱码或无法下载
        name = re.sub(r'[？\\*|“<>:/]', '', name)
        name = re.sub("[A-Za-z0-9\!\%\[\]\,\。\-\?]", "", name)
        name = name.strip()
        filename = u'{}/{}'.format(name, image_guid)
        sql1 = "insert into img values ('{}','{}','{}')"\
                        .format(image_guid,filename,request.url)
        self.cur.execute(sql1)
        self.con.commit()
        self.cur.close()
        self.con.close()
        # self.file.close()

        return filename












