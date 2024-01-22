# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YpScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PlubmerInfo(scrapy.Item):
    name = scrapy.Field()
    phone_number = scrapy.Field()
    website = scrapy.Field()
    street_adress = scrapy.Field()
    genral_info = scrapy.Field()
    #services = scrapy.Field()
    payment_mentod = scrapy.Field()
    stars_out_of_five = scrapy.Field()
    number_of_riews = scrapy.Field()
    email = scrapy.Field()
    locality_ = scrapy.Field()
    full_address = scrapy.Field()
    logo = scrapy.Field()

class RestruantInfo(scrapy.Item):
    name = scrapy.Field()
    phone_number = scrapy.Field()
    website = scrapy.Field()
    street_adress = scrapy.Field()
    genral_info = scrapy.Field()
    #services = scrapy.Field()
    payment_mentod = scrapy.Field()
    stars_out_of_five = scrapy.Field()
    number_of_riews = scrapy.Field()
    email = scrapy.Field()
    locality_ = scrapy.Field()
    full_address = scrapy.Field()
    logo = scrapy.Field()

class ElctrtionInfo(scrapy.Item):
    name = scrapy.Field()
    phone_number = scrapy.Field()
    website = scrapy.Field()
    street_adress = scrapy.Field()
    genral_info = scrapy.Field()
    #services = scrapy.Field()
    payment_mentod = scrapy.Field()
    stars_out_of_five = scrapy.Field()
    number_of_riews = scrapy.Field()
    email = scrapy.Field()
    locality_ = scrapy.Field()
    full_address = scrapy.Field()
    logo = scrapy.Field()