import re

from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, Identity, TakeFirst

from cialdnb.utils import clean_phone


class CialdnbItemLoader(ItemLoader):

    logo_in = MapCompose(str.strip)
    logo_out = TakeFirst()

    phones_in = MapCompose(str, clean_phone)
    phones_out = Identity()

    website_in = MapCompose(str.strip)
    website_out = TakeFirst()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_logo(self, logo):
        if re.search(r'^\/\/.+', logo):
            logo = re.sub(r'^\/\/.+', '', logo)
        elif not re.search(r'^https?:\/\/.+', logo):
            logo = f"https://{self.context.get('response').url.split('/')[2]}/{logo}"

        self.add_value('logo', logo)
