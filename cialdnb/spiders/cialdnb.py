import re
import scrapy

from cialdnb.items.items import CialdnbItem
from cialdnb.items.listing_item_loader import CialdnbItemLoader


class CIALdnbSpider(scrapy.Spider):
    name = 'cialdnb'

    def __init__(self, urls='', **kwargs):
        self.start_urls = self.get_urls(urls)
        super().__init__(**kwargs)

    def get_urls(self, urls):
        if type(urls) is list:
            return urls

        return urls.split()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_items)

    def parse_items(self, response):
        loader = CialdnbItemLoader(item=CialdnbItem(), response=response)
        loader.add_value('website', response.url)

        logo = response.xpath('//img[contains(@src, ".png") or contains(@src, ".jpg") or '
                              'contains(@src, ".jpeg") or contains(@src, ".svg")]//@src').get()
        loader.add_logo(logo)

        phones = re.findall(
            r'\+?\s?\d{0,2}\s\(?\d{1,4}\)?[\s-]\d{2,4}[\s-]\d{2,4}-?\d{2}', response.body.decode('utf-8')
        )
        loader.add_value('phones', set([''.join(p).strip() for p in phones]))

        yield loader.load_item()
