import sys

from cialdnb.spiders.cialdnb import CIALdnbSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    urls = []
    if not sys.stdin.isatty():
        urls = [line.strip() for line in sys.stdin]

    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(CIALdnbSpider, urls=urls)
    process.start()


if __name__ == '__main__':
    main()
