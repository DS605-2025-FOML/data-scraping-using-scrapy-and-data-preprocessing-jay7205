import scrapy
from ..items import Lab2Item

class SpidermanSpider(scrapy.Spider):
    name = 'spiderman'
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        all_div_quotes = response.css('div.quote')

        items= Lab2Item()

        for quotes in all_div_quotes:
            text = quotes.css('span.text::text').extract_first()
            author = quotes.css('author::text').extract_first()
            tag = quotes.css('.tags::text').extract()

            items['text'] = text
            items['author'] = author  
            items['tag'] = tag

            yield items

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
