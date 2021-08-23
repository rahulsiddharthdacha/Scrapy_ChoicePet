# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChoicepetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    StoreName=scrapy.Field()
    Street=scrapy.Field()
    City=scrapy.Field()
    State=scrapy.Field()
    Zipcode=scrapy.Field()
    Country=scrapy.Field()
    Latitude=scrapy.Field()
    Longitude=scrapy.Field()
    Phone=scrapy.Field()
    Duration=scrapy.Field()
    
