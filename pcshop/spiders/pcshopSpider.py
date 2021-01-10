import scrapy
from ..items import PcshopItem


class PcshopScrapy(scrapy.Spider):
    name = 'pcshop'
    start_urls = [
        'https://pcshop.ge/product-category/notebooks/'
    ]

    def parse(self, response, **kwargs):
        items = PcshopItem()
        for nb in response.css('main.site-main ul.products li'):
            items['title'] = nb.css('h2::text').get()
            items['price'] = nb.css('bdi::text').get()

            yield items
        
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)