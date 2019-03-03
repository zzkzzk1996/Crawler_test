# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MyscrapyItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films']

    def parse(self, response):
        names = response.xpath('//div[@class ="channel-detail movie-item-title"]/@title').extract()
        scores = [score.xpath('string(.)').extract_first() for score in
                  response.xpath('//div[@class = "channel-detail channel-detail-orange"]')]
        # for score in scores_div:
        #     scores.append(score.xpath('string(.)').extract_first())

        # use dictionary to push item
        # for name, score in zip(names, scores):
        #     # print(name, ':', score)
        #     yield {"name": name, "score": score}

        # use object to push item
        item = MyscrapyItem()
        for name, score in zip(names, scores):
            item['name'] = name
            item['score'] = score

            if response.url.find('catId=2') != -1:
                item['type'] = 'comedy'
            elif response.url.find('catId=3') != -1:
                item['type'] = 'romantic'
            yield item
