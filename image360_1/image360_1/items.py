# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class ImageItem(Item):
    """docstring for ImageItem"""
    collection = table = 'images'
    id = Field()
    url = Field()
    title = Field()
    thumb = Field()