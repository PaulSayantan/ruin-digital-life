import scrapy
from ..items import SillyhacksItem

class SillySpider(scrapy.Spider):
    name = 'silly'
    start_urls = ['https://www.geckoandfly.com/18885/unmotivated-quotes-friends-enemies-overconfident/']

    def parse(self, response):
        # title=response.css('.entry-title').css('::text').extract()
        items=SillyhacksItem()
        thoughts=response.css('.entry-content p+ p , .adslot_2~ p g').css('::text').extract()
        for thought in thoughts:
            items['thought']=thought
            yield items
        
