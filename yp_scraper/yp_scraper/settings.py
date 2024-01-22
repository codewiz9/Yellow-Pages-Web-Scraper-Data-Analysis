
BOT_NAME = 'yp_scraper'

SPIDER_MODULES = ['yp_scraper.spiders']
NEWSPIDER_MODULE = 'yp_scraper.spiders'

SCRAPEOPS_API_KEY = '6fb2b3fe-45c0-463b-9213-7b370de908f2' 
#SCRAPEOPS_PROXY_ENABLED = True


ROBOTSTXT_OBEY = False


DOWNLOADER_MIDDLEWARES = {
    #'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

ITEM_PIPELINES = {
    'yp_scraper.pipelines.YpScraperPipeline': 300,
}

FEEDS = {
    'yp_data.csv': {'format': 'csv'},
}

#CONCURRENT_REQUESTS = 1
