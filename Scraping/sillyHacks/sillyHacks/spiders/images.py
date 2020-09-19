import scrapy
from ..items import SillyhacksImage

class SillySpider(scrapy.Spider):
    name = 'images'
    start_urls = ['https://www.geckoandfly.com/18885/unmotivated-quotes-friends-enemies-overconfident/']

    def parse(self, response):
        # title=response.css('.entry-title').css('::text').extract()
        items=SillyhacksImage()
        images=response.css('.entry-content p+ p').css('img').css('::attr("src")').extract()
        print(images)
        for image in images:
            print(image)
            items['image']=image
            yield items
        
