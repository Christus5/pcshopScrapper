import scrapy

class PcshopScrapy(scrapy.Spider):
    name = 'pcshop'
    allowed_domains = ['https://pcshop.ge/']