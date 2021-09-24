

import pymysql


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


def close_spider(self, spider):
    self.cursor.close()
    self.connect.close()

