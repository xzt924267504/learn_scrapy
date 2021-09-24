import scrapy
from scrapy.http import Request
from ..items import GifzzzItem
# from scrapy.spider import Spider
class SbSpider(scrapy.Spider):
    name = 'sb'
    allowed_domains = ['www.gifzzz.com']
    start_urls = ['http://www.gifzzz.com/']

    def parse(self, response):
        """
        列表所有标题的url及标题text
        :param response:
        :return:
        """
        a = response.css('.thread-list')
        # 标题href
        listurl = a.css('.thread-title::attr(href)').getall()
        # flie_name = a.css('.thread-title::text').getall()

        for i in listurl:
            yield Request(i,callback=self.parse2)


    def parse2(self,response):
        b = response.css('.content.typo.editor-style.thread-content')
        img_url = b.css('img::attr(data-src)').getall()
        flie_name = response.xpath('/html/head/title').get()

        item = GifzzzItem()
        item['img_url'] = img_url
        item['flie_name'] = flie_name

        yield item





