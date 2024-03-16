# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()

    name = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    product_type = scrapy.Field()
    star_rating = scrapy.Field()
    pass
