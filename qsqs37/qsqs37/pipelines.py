
import pymysql
from itemadapter import ItemAdapter
# from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import re

class Qsqs37Pipeline:

    def process_item(self, item, spider):
        # 数据库连接
        self.con = pymysql.connect(
            host='127.0.0.1',  #服务器IP
            port=3306,  # 服务器端口号:不是字符串不需要加引号。
            user='root',
            password='123456',
            db='qsqs37',
            charset='utf8')
        # 得到一个可以执行SQL语句的光标对象
        self.cur = self.con.cursor()  # 执行完毕返回的结果集默认以元组显示
        print(spider.name, '打开数据库连接，爬虫开始了...')

        #过滤标题中的特殊字符
        biaoti = item["xs_name"]
        re.sub(r'[？\\*|“<>:/：]', '', biaoti)
        re.sub("[A-Za-z0-9\!\%\[\]\,\。\-\?]", "", biaoti)
        biaoti.strip()

        #过滤正文特殊字符
        zhengwen = item["xs_zhengwen"]
        zhengwen = zhengwen.replace(r'<div class="nbodys">','')
        zhengwen = zhengwen.replace(r'</div>', '')
        new_zhengwen = zhengwen.replace(r'<br>', '')

        #保存小说
        xs_name_lujing = r"D:\python_file\sc\qsqs37\xiaoshuo4\xuanhuan\{}.txt".format(biaoti)
        with open(xs_name_lujing, 'a', encoding='utf-8') as f:
            f.write(item["xs_name"])
            f.write('\n')
            f.write('\n')
            f.write(new_zhengwen)
            f.write('\n')
            f.write('\n')

        sql1 = "insert into xiaoshuo values ('{}','{}','{}','{}')" \
            .format( item["xs_name"],xs_name_lujing ,item["xs_url"],'玄幻武侠')
        self.cur.execute(sql1)
        self.con.commit()
        self.cur.close()
        self.con.close()
        # self.file.close()
        # print(spider.name, '数据库连接关闭，爬虫结束了...')
        return item












