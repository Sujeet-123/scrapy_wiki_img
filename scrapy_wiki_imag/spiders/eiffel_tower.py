# -*- coding: utf-8 -*-
import scrapy


class EiffelTowerSpider(scrapy.Spider):
    name = 'eiffel_tower'
    # allowed_domains = ['www.xyz.com']
    start_urls = ['https://en.wikipedia.org/wiki/Eiffel_Tower']

    def parse(self, response):
        raw_image_urls = response.css('.image img ::attr(src)').getall()
        clean_image_urls = []

        for img in raw_image_urls:
            clean_image_urls.append(response.urljoin(img))
    

        yield{
            'image_urls': clean_image_urls
        }