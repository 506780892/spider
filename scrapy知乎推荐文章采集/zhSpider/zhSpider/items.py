# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhspiderItem(scrapy.Item):
    title = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()


if __name__ == '__main__':
    print(ZhspiderItem.__dict__['fields'].keys())