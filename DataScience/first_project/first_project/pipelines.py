# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FirstProjectPipeline:
    def process_item(self, item, spider):
        print("++++++++++++ pipie1")
        adapter = ItemAdapter(item)
        restaurant_name = adapter.get("restaurant_name")
        if restaurant_name is not None:
            adapter["restaurant_name"] = restaurant_name.strip()
        address = adapter.get("address")
        if address is not None:
            adapter["address"] = address.strip()
        return item


class FirstProjectPipeline2:
    def process_item(self, item, spider):
        print("++++++++++++ pipie2")
        return item
