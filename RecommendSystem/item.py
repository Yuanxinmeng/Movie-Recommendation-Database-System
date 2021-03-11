import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    movie_sysnopsis = scrapy.Field()
    movie_score = scrapy.Field()
    type = scrapy.Field()
