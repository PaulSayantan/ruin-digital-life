# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SillyhacksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    thought=scrapy.Field()


class SillyhacksImage(scrapy.Item):
    image=scrapy.Field()