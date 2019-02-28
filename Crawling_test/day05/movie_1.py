import requests
from fake_useragent import UserAgent
from lxml import etree
from random import randint
from time import sleep


def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome
    }
    sleep(randint(3, 10))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_index(html):
    e = etree.HTML(html)
    all_urls = e.xpath('//div[@class = "channel-detail movie-item-title"]/a/@href')
    return ["https://maoyan.com{}".format(url) for url in all_urls]


def parse_info(html):
    e = etree.HTML(html)
    name = e.xpath('//h3[@class = "name"]/text()')[0]
    type = e.xpath('//li[@class ="ellipsis"][1]/text()')[0]
    actors = e.xpath('//li[@class="celebrity actor"]/div[@class="info"]/a/text()')
    actors = format_data(actors)
    return {
        "name": name,
        "type": type,
        "actors": actors
    }


def format_data(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.strip())
    return actor_set


def main():
    index_url = "https://maoyan.com/films"
    html = get_html(index_url)
    movie_urls = parse_index(html)
    # print(movie_urls)
    for url in movie_urls:
        movie_html = get_html(url)
        movie = parse_info(movie_html)
        print(movie)


if __name__ == '__main__':
    main()
