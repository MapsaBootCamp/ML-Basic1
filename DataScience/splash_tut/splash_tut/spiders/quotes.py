from typing import Iterable
import scrapy
from scrapy.http import Request
from scrapy_splash import SplashRequest


lua_script = """
function main(splash, args)
  local get_div_count = splash:jsfunc([[
  function () {
    var body = document.body;
    var divs = body.getElementsByTagName('div');
    return divs.length;
  }
  ]])
  splash:go(args.url)

  return ({html=("There are %s DIVs in %s"):format(
    get_div_count(), args.url)})
end
"""


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/js/"]

    def start_requests(self) -> Iterable[Request]:
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={"wait": 0.5, "lua_source": lua_script})

    def parse(self, response):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(response.body)

        # quotes = response.css("div.quote").getall()

        # for quote in quotes:
        #     yield {
        #         quote: response.css("span.text::text").get()
        #     }
