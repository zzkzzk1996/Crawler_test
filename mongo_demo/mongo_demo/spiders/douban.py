# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start={}&filter='.format(num * 25) for num in range(10)]

    def parse(self, response):
        names = response.xpath('//div[@class="info"]//a/span[1]/text()').extract()
        stars = response.xpath('//div[@class="info"]//div[@class="star"]/span[2]/text()').extract()
        for name, star in zip(names, stars):
            yield {
                "name": name,
                "star": star
            }
