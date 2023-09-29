import scrapy


class HarchiSpider(scrapy.Spider):
    name = "harchi"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
