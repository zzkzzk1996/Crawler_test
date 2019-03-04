# -*- coding: utf-8 -*-
import scrapy


class HuangjintongSpider(scrapy.Spider):
    name = 'huangjintong'
    allowed_domains = ['luoxia.com']
    start_urls = ['http://www.luoxia.com/huangjintong/70141.htm']

    def parse(self, response):
        title = response.xpath('//h1[@id="nr_title"]/text()').extract_first()
        content = '\n\t'.join(response.xpath('//div[@id="nr1"]/p/text()').extract())

        yield {
            'title': title, 'content': content
        }
        next_url = response.xpath('//nav[@class="nav2 bbn mb2 clearfix"]//li[@class="next"]/a/@href').extract_first()
        if next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse)
