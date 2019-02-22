import requests
from fake_useragent import UserAgent
from lxml import etree

url = "http://www.farmer.com.cn/xwpd/rdjj1/201807/t20180726_1393916.htm"

headers = {
    "User-Agent": UserAgent().chrome
}

response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
title = e.xpath('//h1/text()')
all_p_tag = e.xpath('//div[@class = "content"]//p')
content = []
for p in all_p_tag:
    info = p.xpath('string(.)')
    content.append(info)
content_str = ''.join(content)
img_urls = e.xpath('//div[@class = "content"]//img/@src')
img_names = e.xpath('//div[@align = "center"]')
for num in range(1, len(img_names), 2):
    img_name = img_names[num].xpath('string(.)')
