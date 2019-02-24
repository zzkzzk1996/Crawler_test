# 1st version of crawler for 'zeenews'

# import libraries
import requests
from fake_useragent import UserAgent
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import subprocess


# get html
def get_html():
    # url link
    url = "https://zeenews.india.com/hindi/india/bihar-jharkhand/video/randhir-singhs-exclusive-interview/501251"
    # headers for requests
    headers = {
        "User-Agent": UserAgent().random
    }
    # request and get html in response
    response = requests.get(url, headers=headers)
    code = response
    # return raw html wait for decrypt
    return code


def decrypt_html(code):
    # soup = BeautifulSoup(code, "lxml")
    # # print(soup.div)
    # # print(soup.find_all("div", id='preview-501255'))
    # print(soup.find_all(id='preview-501255'))
    e = etree.HTML(code.text)
    video_url = e.xpath('string(//div/@video-code)')
    print(video_url)
    return video_url


def video_extract(url):
    subprocess.check_call(["ffmpeg", "-i",  url, "-vcodec", "copy", "-acodec", "copy", "-absf", "aac_adtstoasc", "test_hindi.mp4"])


if __name__ == '__main__':
    code = get_html()
    url = decrypt_html(code)
    video_extract(url)