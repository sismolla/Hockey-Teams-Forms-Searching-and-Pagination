# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HockeyteamsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    Wins = scrapy.Field()
    losses = scrapy.Field()
    ot_losses = scrapy.Field()
    win_percent = scrapy.Field()
    goals_for_GF = scrapy.Field()
    goals_aginest = scrapy.Field()
    diff_text_success = scrapy.Field()
    pass
