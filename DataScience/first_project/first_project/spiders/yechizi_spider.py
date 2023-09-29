import scrapy
# from urllib.parse import urlparse
from first_project.items import RestaurantItem, RestaurantItemDataClass


class FidioSpider(scrapy.Spider):
    name = "Fidio"
    allowed_domains = ["fidilio.com"]
    custom_settings = {
        "FEEDS": {
            'ghoalm.csv': {
                'format': 'csv',
                'store_empty': False,
            }
    }

    }
    start_urls = [
        "https://fidilio.com/restaurants/in/tehran/%D8%AA%D9%87%D8%B1%D8%A7%D9%86/"
    ]

    def parse(self, response):
        items_per_page = response.css(
            '.justify-self-center.justify-center.items-center.mt-6.min-w-fit')
        for item in items_per_page:
            href = item.css('a::attr("href")').get()
            if href:
                # uri = urlparse(response.url)
                # domain = f"{uri.scheme}://{uri.netloc}"
                yield response.follow(response.urljoin(href),
                                      callback=self.parse_detail_restaurant)  # Request
        next_page = response.css(
            'button.bg-fidilio-red.w-full.text-white.py-2.px-4.rounded-full').xpath("..").attrib["href"]
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page))

    def parse_detail_restaurant(self, response):
        item = RestaurantItem()
        restaurant_name = response.css(
            "p.text-base.venue-name.line-clamp-1.text-white.mt-14::text").get()
        status = response.css("p.text-white.text-sm::text").get()
        address = response.css(
            "p.text-fidilio-dark-gray.mx-2.line-clamp-2::text").get()
        if status is not None:
            item["restaurant_name"] = restaurant_name
            item["status"] = status
            item["address"] = address
            yield item
            # yield RestaurantItemDataClass(restaurant_name, status, address)
