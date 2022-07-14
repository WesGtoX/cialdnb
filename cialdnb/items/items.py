import scrapy


class CialdnbItem(scrapy.Item):
    logo = scrapy.Field()
    phones = scrapy.Field()
    website = scrapy.Field()
