import scrapy
from ..items import AllimgItem
from scrapy.http import Request
class DoallimgSpider(scrapy.Spider):
    name = 'doallimg'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']
    """
    text = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    tags = scrapy.Field()
    author_img_url = scrapy.Field()
    """
    def parse(self, response):
        author_url = response.css('.quote.post span a::attr(href) ').getall()
        text = response.css('[class="text"]::text').getall()
        author = response.css('[class="author"]::text').getall()

        for list_url in author_url:
            yield Request(list_url,callback=self.parse2)

        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            # 下一页
            yield response.follow(next_page, callback=self.parse)

    def parse2(self, response):
        item = AllimgItem()
        item['author_img_url'] = response.css('.post img::attr(src)').getall()
        yield item




# //*[@id="hellobox"]/div[2]/div/a[2]