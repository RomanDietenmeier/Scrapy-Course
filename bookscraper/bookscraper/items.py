# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


def fix_star_rating(star_rating: str):
    if "one" in star_rating.lower():
        return 1
    elif "two" in star_rating.lower():
        return 2
    elif "three" in star_rating.lower():
        return 3
    elif "four" in star_rating.lower():
        return 4
    elif "five" in star_rating.lower():
        return 5
    else:
        return star_rating


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()

    name = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    product_type = scrapy.Field()
    star_rating = scrapy.Field(serializer=fix_star_rating)
    pass
