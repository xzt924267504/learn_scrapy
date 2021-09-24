import scrapy


class PinglunSpider(scrapy.Spider):
    name = 'pinglun'
    allowed_domains = ['asoulcnki.asia']
    start_urls = ['http://asoulcnki.asia/']

    def parse(self, response):
        pass
