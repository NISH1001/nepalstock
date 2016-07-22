# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NepalstockItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    total_transactions = scrapy.Field()
    total_traded_shares = scrapy.Field()
    total_traded_amount = scrapy.Field()
    max_price = scrapy.Field()
    min_price = scrapy.Field()
    close_price = scrapy.Field()
