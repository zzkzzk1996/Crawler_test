from selenium import webdriver
from lxml import etree
from time import sleep

url = "https://search.jd.com/Search?keyword=macbook&enc=utf-8&wq=macbook&pvid=3e90d3f3c2b24f1895ee48fe618416c5"

driver = webdriver.Chrome()
driver.get(url)

js = 'document.documentElement.scrollTop = 100000'
driver.execute_script(js)
sleep(10)

html = driver.page_source

e = etree.HTML(html)
prices = e.xpath('//div[@class = "gl-i-wrap"]/div[@class = "p-price"]/strong/i/text()')
names = e.xpath('//div[@class = "gl-i-wrap"]/div[@class = "p-name p-name-type-2"]/a/em')


print(len(names))
for name, price in zip(names, prices):
    print(name.xpath('string(.)'), ":", price)
