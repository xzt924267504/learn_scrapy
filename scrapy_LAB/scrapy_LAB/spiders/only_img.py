import scrapy
from ..items import ScrapyLabItem

class OnlyImgSpider(scrapy.Spider):
    name = 'only_img'
    allowed_domains = ['lab.scrapyd.cn/']
    start_urls = ['http://lab.scrapyd.cn/archives/57.html/']

    def parse(self, response):
        item = ScrapyLabItem()
        item['author_img_url'] = response.css('.post img::attr(src)').getall()
        # item['author'] = response.css('.post-title a::text').get()
        # print(item)
        yield item


