# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GudongSpider(CrawlSpider):
    name = 'gudong'
    allowed_domains = ['luoxia.com']
    start_urls = ['http://www.luoxia.com/gudong/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="book-list clearfix"][1]//li[1]/a'), callback='parse_item',
             follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//nav[@class= "nav2 bbn mb2 clearfix"]//li[@class="next"]/a'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//h1[@id="nr_title"]/text()').extract_first()
        content = '\n\t'.join(response.xpath('//div[@id="nr1"]/p/text()').extract())

        yield {
            'title': title, 'content': content
        }
