# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class T66YItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    list_url = scrapy.Field()
    list_name = scrapy.Field()
    img_url = scrapy.Field()
    flie_name = scrapy.Field()
    pass
