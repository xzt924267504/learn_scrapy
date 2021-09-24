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

class ZhijiangzuowenPipeline:
    # (ImagesPipeline)

    def process_item(self, item, spider):
        # 数据库连接
        self.con = pymysql.connect(
            host='127.0.0.1',  #服务器IP
            port=3306,  # 服务器端口号:不是字符串不需要加引号。
            user='root',
            password='123456',
            db='database',
            charset='utf8')
        # 得到一个可以执行SQL语句的光标对象
        self.cur = self.con.cursor()  # 执行完毕返回的结果集默认以元组显示
        print(spider.name, '打开数据库连接，爬虫开始了...')










        #re.sub(r'[？\\*|“<>:/]', '', name)
        #re.sub("[A-Za-z0-9\!\%\[\]\,\。\-\?]", "", name)
        #name.strip()
        sql1 = ""
        self.cur.execute(sql1)
        self.con.commit()
        self.cur.close()
        self.con.close()
        # self.file.close()
        print(spider.name, '数据库连接关闭，爬虫结束了...')
        return item




