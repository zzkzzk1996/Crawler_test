# 2nd version of crawler for 'zeenews'
# update for text crawler and selenium webdriver

# import libraries
import requests
from fake_useragent import UserAgent
from selenium import webdriver
from lxml import etree
import subprocess


# use the selenium web driver to get the source page
def web_driver():
    mainpage_url = "https://zeenews.india.com/hindi/videos"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(mainpage_url)
    first_html = driver.page_source
    # print(first_html)
    driver.quit()
    return first_html


# get the mainpage urls
def get_urls(url_source):
    e = etree.HTML(url_source)
    urls = []
    base_url = "https://zeenews.india.com{}"
    for url in e.xpath('//div[@class = "mini-video mini-video-h margin-bt30px"]/a/@href'):
        urls.append(base_url.format(url))
    return urls


# get html
def get_html(url):
    # url link
    # url = "https://zeenews.india.com/hindi/india/bihar-jharkhand/video/randhir-singhs-exclusive-interview/501251"
    # headers for requests
    headers = {
        "User-Agent": UserAgent().random
    }
    # request and get html in response
    response = requests.get(url, headers=headers)
    code = response
    # return raw html wait for decrypt
    return code


# parse the html and return data in txt and video url
def parse_html(code):
    # soup = BeautifulSoup(code, "lxml")
    # # print(soup.div)
    # # print(soup.find_all("div", id='preview-501255'))
    # print(soup.find_all(id='preview-501255'))
    e = etree.HTML(code.text)
    video_url = e.xpath('string(//div/@video-code)')
    title = "".join(e.xpath('//div/h1/text()'))
    text = "".join(e.xpath('//div/p[@class="margin-bt10px"]/text()'))
    print(video_url)
    print(title + '\n' + text)
    return title, text, video_url


def save_text(title, text):
    with open('Zeenews_text.txt', 'a', encoding='utf-8') as f:
        f.write(title)
        f.write(text)


# using ffmpeg in the terminal to extract the video and transform the video
def video_extract(video_url, number):
    subprocess.check_call(
        ["ffmpeg", "-i", video_url, "-vcodec", "copy", "-acodec", "copy", "-absf", "aac_adtstoasc",
         "hindi_" + str(number) + ".mp4"])


if __name__ == '__main__':
    url_source = web_driver()
    urls = get_urls(url_source)
    number = 0
    for url in urls:
        number = number + 1
        code = get_html(url)
        title, text, video_url = parse_html(code)
        save_text(title, text)
        video_extract(video_url, number)
        if number == 5:
            break
