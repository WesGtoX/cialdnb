# Scrapy settings for cialdnb project
BOT_NAME = 'cialdnb'

SPIDER_MODULES = ['cialdnb.spiders']
NEWSPIDER_MODULE = 'cialdnb.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

FEED_FORMAT = 'json'
FEED_URI = 'cialdnb.json'

FEED_STORAGES_BASE = {
    '': 'cialdnb.customexport.OverwriteFileFeedStorage',
    'file': 'cialdnb.customexport.OverwriteFileFeedStorage',
}
