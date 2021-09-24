import time
import pymysql
import requests
import json
from pymysql.converters import escape_string
class Zhijiang():
  def __init__(self):
    self.url = "https://asoulcnki.asia/v1/api/ranking/?pageSize=10&pageNum=1&timeRangeMode=0&sortMode=0&ids=&keywords="

    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'
    }
  #处理接口返回的数据
  def data(self):
    response = requests.get(self.url, headers=self.headers)

    # 接口返回的所有数据
    re_text = json.loads(response.text)
    re_data = re_text.get('data')
    #每个用户的信息以及发言
    re_replies = re_data.get('replies')

    #  格式例子https://www.bilibili.com/video/av589913922/#reply5210584309
    #         https://t.bilibili.com/472642570902204872/#reply3866856390


    for i in  re_replies:
      time.sleep(2)
      content = i.get('content')
      content = escape_string(content)
      content = content.replace(r'\n','换行符123')
      # print(content)
      m_name = i.get('m_name')
      rpid = i.get('rpid')            # 后
      oid = i.get('oid')              # 前
      type_id = i.get('type_id')      #id为1是av号, 17是发的动态
      if type_id == 1:
        # root_url = "www.bilibili.com/video/av{}/井号reply{}".format(oid,rpid)
        sql = "insert into pinglun (m_name,content,rpid,oid,type_id) values ('{}','{}','{}','{}','{}')".format(
          m_name, content, rpid, oid, type_id)
      elif type_id == 17:
        # root_url = "t.bilibili.com/{}/井号reply{}".format(oid,rpid)
        sql = "insert into pinglun (m_name,content,rpid,oid,type_id) values ('{}','{}','{}','{}','{}')".format(
          m_name, content, rpid, oid, type_id)
      else:
        print("typeid错误 type_id:'{}'".format(type_id))
        print(m_name)
        continue
      print(sql)
      self.write_db(sql)



  # 数据库写入
  def write_db(self, sql, database='zhijiang', host='127.0.0.1', user='root', password='123456', ):
    con = pymysql.connect(host=host, user=user, password=password, database=database, port=3306)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
    cur.close()



if __name__ == '__main__':
  z = Zhijiang()
  z.data()
