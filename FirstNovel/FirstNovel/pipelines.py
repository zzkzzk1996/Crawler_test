# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstnovelPipeline(object):
    def open_spider(self, spider):
        self.file = open('古董局中局.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        data = title + '\n\n' + content + '\n\n'
        self.file.write(data)
        return item

    def close_spider(self, spider):
        self.file.close()
