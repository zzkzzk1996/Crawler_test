import requests
from fake_useragent import UserAgent
from lxml import etree


# manage url
class URLManager():
    def __init__(self):
        self.new_url = []
        self.ori_url = []

    # get url
    def get_new_url(self):
        url = self.new_url.pop()
        self.ori_url.append(url)
        return url

    # add url
    def add_new_url(self, url):
        if url not in self.new_url and url not in self.ori_url:
            self.new_url.append(url)

    # add url array
    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)

    # judge whether there are urls can be crawled
    def has_new_url(self):
        return self.get_new_url_size() > 0

    # get the numbers of urls can be crawled
    def get_new_url_size(self):
        return len(self.new_url)

    # get the numbers of crawled urls
    def get_ori_url_size(self):
        return len(self.ori_url)


# crawling
class Downloader:
    def download(self, url):
        response = requests.get(url, headers={"User-Agent": UserAgent().random})
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            return None


# parse
class Parser:
    def parse(self, html):
        e = etree.HTML(html)
        data = self.parse_info(e)
        urls = self.parse_url(e)
        return data, urls

    def parse_info(self, e):
        data_spans = e.xpath('//div[@class = "content"]/span')
        data = []
        for data_span in data_spans:
            data.append(data_span.xpath('string(.)'))
        return data

    def parse_url(self, e):
        base_url = "https://www.qiushibaike.com{}"
        urls = []
        for url in e.xpath('//ul[@class = "pagination"]/li/a/@href'):
            urls.append(base_url.format(url))
        return urls


# dealing data
class DataOutPut:
    def save(self, data):
        with open('duanzi.txt', 'a', encoding='utf-8') as f:
            for data in data:
                f.write(data)


# control
class Controller:
    def __init__(self):
        self.downloader = Downloader()
        self.url_manager = URLManager()
        self.parser = Parser()
        self.data_saver = DataOutPut()

    def run(self, url):
        self.url_manager.add_new_url(url)
        while self.url_manager.has_new_url():
            url = self.url_manager.get_new_url()
            html = self.downloader.download(url)
            data, urls = self.parser.parse(html)
            self.data_saver.save(data)
            self.url_manager.add_new_urls(urls)


if __name__ == '__main__':
    Controller = Controller()
    Controller.run("https://www.qiushibaike.com/text/page/1/")
