import scrapy
from yp_scraper.items import PlubmerInfo

class PlumberScraperSpider(scrapy.Spider):
    name = 'plumber_scraper'
    allowed_domains = ['yellowpages.com']
    start_urls = ['https://www.yellowpages.com/']

    def parse(self, response):
        #bellow are the area name and state these values will be plued into the start url to find the area in wich we are serchign for plumbers
        area = "fairfax"
        state = "va"#must be an abreation
        #the value bellow is the amount of pages you want to scrape
        numer_of_pages = 1 
        page_numebr = 1
        while numer_of_pages > 0:
            url = f'https://www.yellowpages.com/{area}-{state}/plumbers?page={page_numebr}'
            page_numebr += 1
            numer_of_pages -= 1
            yield response.follow(url, callback=self.parse_plumbers)

    def parse_plumbers(self, response):
        print('text2')
        plumber_item = PlubmerInfo()
        print('yes_man')
        plumbers = response.css('div.result')

        for plumber in plumbers:
            starter_indidual_url = plumber.css('a.business-name ::attr(href)').get()
            indidual_url = f'https://www.yellowpages.com{starter_indidual_url}'
            yield response.follow(indidual_url, callback=self.parse_indvidual_plumbers)

    def parse_indvidual_plumbers(self, response):
        x = response.css('span.address ::text').get()
        y = response.xpath('//*[@id="default-ctas"]/a[3]/span/text()').get()
        plumber_item = PlubmerInfo()
        plumber_item['name'] = response.css('h1.business-name ::text').get()
        plumber_item['phone_number'] = response.css('a.phone ::text').get() 
        plumber_item['website'] = response.css('a.website-link ::attr(href)').get()
        plumber_item['genral_info'] = response.css('dd.general-info ::text').get()
        plumber_item['payment_mentod'] = response.css('dd.payment ::text').get()
        plumber_item['stars_out_of_five'] = response.css('div.rating-stars ::attr(class)').get()
        plumber_item['number_of_riews'] = response.css('span.count ::text').get()
        plumber_item['locality_'] = response.xpath('//*[@id="default-ctas"]/a[3]/span/text()').get()
        plumber_item['street_adress'] = response.css('span.address ::text').get()
        plumber_item['email'] = response.css('a.email-business ::attr(href)').get()
        plumber_item['full_address'] =  f'{x} {y}'
        plumber_item['logo'] = response.css('dd.logo ::attr(href)').get()

        yield plumber_item 
