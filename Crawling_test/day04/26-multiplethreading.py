from threading import Thread
from queue import Queue
from fake_useragent import UserAgent
import requests
from lxml import etree


# crawling class
class CrawlInfo(Thread):
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        headers = {
            "User-Agent": UserAgent().chrome
        }
        while self.url_queue.empty() == False:
            response = requests.get(self.url_queue.get(), headers=headers)
            if response.status_code == 200:
                self.html_queue.put(response.text)
            # print(response.text)


# parse class
class ParseInfo(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue

    def run(self):
        while self.html_queue.empty() == False:
            e = etree.HTML(self.html_queue.get())
            span_contents = e.xpath('//div[@class = "content"]/span[1]')
            with open("duanzi.txt", 'a', encoding='utf-8') as f:
                for span in span_contents:
                    info = span.xpath('string(.)')
                    f.write(info + '\n')


if __name__ == '__main__':
    # container for saving url
    url_queue = Queue()
    # container for saving contents
    html_queue = Queue()
    base_url = "https://www.qiushibaike.com/text/page/{}/"
    for i in range(1, 14):
        new_url = base_url.format(i)
        url_queue.put(new_url)
    crawler_list = []
    # create a crawler
    for i in range(0, 3):
        crawler1 = CrawlInfo(url_queue, html_queue)
        crawler_list.append(crawler1)
        crawler1.start()

    for crawl in crawler_list:
        crawl.join()

    parse_list = []
    for i in range(0,3):
        parse = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()
    for parse in parse_list:
        parse.join()
