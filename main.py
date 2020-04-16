from scrapy.crawler import CrawlerProcess
from ParseTauntondeeds.ParseTauntondeeds.spiders import crawled_deeds

# start scrapy
proces = CrawlerProcess(settings={'FEED_FORMAT': 'json', 'FEED_URI': 'item.jl'})
proces.crawl(crawled_deeds.CrawledDeedsSpider)
proces.start()
