# -*- coding: utf-8 -*-
import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    # start_urls = ['https://www.qidian.com/rank/yuepiao']

    def start_requests(self):
        # base_url = 'https://www.qidian.com/rank/yuepiao'
        yield scrapy.Request('https://www.qidian.com/rank/yuepiao')

    def parse(self, response):
        names = response.xpath('//h4/a/text()').extract()
        authors = response.xpath('//p[@class= "author"]/a[1]/text()').extract()
        # print(names)
        # print(authors)
        novel = []
        for name, author in zip(names, authors):
            novel.append({'name': name, 'author': author})
        return novel
