import scrapy
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from ..items import Qsqs37Item

# CrawlSpider
class XsSpider(scrapy.Spider):
    name = 'xs'
    allowed_domains = ['015caiji.com']
    start_urls = [
        # 'https://www.015caiji.com/textlist/14/836-1.html', #1
        # 'https://www.015caiji.com/textlist/14/837-1.html',  #1
        # 'https://www.015caiji.com/textlist/14/838-1.html',  #1
        # 'https://www.015caiji.com/textlist/14/839-1.html',  #11111111111
        # 'https://www.015caiji.com/textlist/14/840-1.html',  #1
        'https://www.015caiji.com/textlist/14/841-1.html',  #1
        # 'https://www.015caiji.com/textlist/14/842-1.html',  #1
        # 'https://www.015caiji.com/textlist/14/843-1.html',  #1
    ]


    def parse(self, response):
        url_list = response.css('.name a::attr(href)').getall()
        for i in url_list:
            url1 = 'https://www.015caiji.com' + i
            yield Request (url1,callback=self.parse2)

        # 下一页
        next_page = response.css('.pager div a::attr(href)').getall()[-2]
        last_page = response.css('.pager div a::attr(href)').getall()[-1]
        next_page_url = 'https://015caiji.com' + next_page
        if next_page != last_page:
            next_page1 = response.urljoin(next_page_url)
            yield scrapy.Request(next_page1, callback=self.parse)


    def parse2(self,response):
        xs_name = response.css('.title::text').get()
        xs_zhengwen = response.css('.nbodys').get()
        xs_url = response.url

        item = Qsqs37Item()
        item["xs_name"] = xs_name
        item["xs_zhengwen"] = xs_zhengwen
        item["xs_url"] = xs_url

        yield item
















#