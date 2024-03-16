# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        field_names = adapter.field_names()
        for field_name in field_names:
            if adapter.get(field_name) is None:
                adapter[field_name] = "N/A"
            adapter[field_name] = adapter[field_name].strip()
        adapter["url"] = adapter["url"].lower()
        return item
