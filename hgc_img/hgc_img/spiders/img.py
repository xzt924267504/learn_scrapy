import scrapy
from ..items import HgcImgItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['yj1.d0ea258blal.club']
    start_urls = [
                    'http://yj1.d0ea258blal.club/pw/html_data/21/2107/5399793.html',

                  ]

    def parse(self, response):
        item = HgcImgItem()
        item['img_url'] = response.css(".f14 img::attr(src)").getall()
        item['flie_name'] = response.css('span#subject_tpc::text').get()

        yield item
