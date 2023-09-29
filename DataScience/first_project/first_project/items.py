# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass
import scrapy


class FirstProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def serilize_status(value):
    return True


class RestaurantItem(scrapy.Item):
    restaurant_name = scrapy.Field()
    # status = scrapy.Field(serializer=serilize_status)
    status = scrapy.Field()
    address = scrapy.Field()


@dataclass
class RestaurantItemDataClass:
    restaurant_name: str
    status: str
    address: str
