import scrapy
from scrapy.http import Request
from ..items import T66YItem

class A1024Spider(scrapy.Spider):
    name = '1024'
    allowed_domains = ['cl.352x.xyz']
    start_urls = [

                    'https://cl.352x.xyz/thread0806.php?fid=8',
                    # 'https://cl.352x.xyz/thread0806.php?fid=8&search=&page=2',

                  # 'https://cl.352x.xyz/htm_data/2106/8/4528344.html',
                  # 'https://cl.352x.xyz/htm_data/2106/8/4536439.html',
                  # 'https://cl.352x.xyz/htm_data/2106/8/4536408.html'
    ]


    def parse(self, response):
        aa = response.xpath('//tbody[@id="tbody"]')
        listurl = aa.css('.tr3.t_one.tac h3 a::attr(href)').getall()

        for url in listurl:
            url2 = 'https://cl.352x.xyz/'+url
            # print(url2)
            yield Request(url2,callback=self.parse2)

    def parse2(self,response):
        item = T66YItem()
        item['img_url'] = response.css('.tpc_content.do_not_catch img::attr(ess-data)').getall()
        item['flie_name'] = response.css('.f16::text').get()

        yield item














    """
    def parse(self, response):
        item = T66YItem()

        item['img_url'] = response.css('.tpc_content.do_not_catch img::attr(ess-data)').getall()

        yield item


    """

