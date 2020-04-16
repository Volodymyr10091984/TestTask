# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
from typing import List


# Data serialization function date
def serialize_date(value: List[str]) -> List[str]:
    date_list = value
    data_result = list()
    for date in date_list:
        date_second = date.split('/')
        date_dat = datetime.date(int(date_second[2]), int(date_second[0]), int(date_second[1]))
        data_result.append(datetime.date.strftime(date_dat, '%d/%m/%y'))
    return data_result


# Data serialization function book and page_num
def serialize_book(value: List[str]) -> List[str]:
    result = []
    for i in value:
        if i == '\u00a0':
            result.append('None')
        else:
            result.append(i)
    return result


class ParsetauntondeedsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field(serializer=serialize_date)
    type = scrapy.Field()
    book = scrapy.Field(serializer=serialize_book)
    page_num = scrapy.Field(serializer=serialize_book)
    doc_num = scrapy.Field()
    city = scrapy.Field()
    description = scrapy.Field()
    cost = scrapy.Field()
    street_address = scrapy.Field()
    state = scrapy.Field()
    zip = scrapy.Field()
