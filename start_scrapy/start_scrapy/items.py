# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy.item


class StartScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class YTTitleItem(scrapy.Item):
    name = scrapy.Field() # #header-container h2#header #title::text
    url = scrapy.Field() # null or url about 'name' field
    elements = scrapy.Field() # YTElementItem list

    def __str__(self) -> str:
        return f"name: {self.name}, url: {self.url}, eles: {self.elements}"

"""
blabafafasf
"""
class YTElementItem(scrapy.Item):
    url = scrapy.Field() # video link
    name = scrapy.Field() # video's title