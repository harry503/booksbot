# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = [
        'https://www.lazada.co.id/catalog/?q=gasol%20merah%20wangi',
    ]

 	def parse(self, response):
        for sel in response.xpath('//div'):
            item = {}
            item['name'] = sel.xpath('//a/text()').extract()
            item['link'] = sel.xpath('//a/@href').extract()

            yield item
