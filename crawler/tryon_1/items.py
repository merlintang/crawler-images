# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TryonItem(scrapy.Item):
    # define the fields for your item here like:

    #clothes name
    id = scrapy.Field()

    name = scrapy.Field()

    designer = scrapy.Field()

    imageUrl = scrapy.Field()

    imageUrlOthers = scrapy.Field()

    details = scrapy.Field()

    url = scrapy.Field()

    price = scrapy.Field()

    category = scrapy.Field()


