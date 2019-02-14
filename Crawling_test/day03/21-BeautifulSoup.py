import requests
from bs4 import BeautifulSoup, Comment

str = '''
<title id="title" class='info'>幽默笑话大全_爆笑笑话_笑破你的肚子的搞笑段子 - 糗事百科</title>
<strong><!--fun--></strong>
'''

soup = BeautifulSoup(str, 'lxml')

print(soup.title)
print(soup.div)  # get all div including attributes
print(soup.div.attrs)  # get all attributes from div
print(soup.div.get('class'))  # get the very attributes from the div
print(soup.div['class'])  # same

print(soup.a['href'])

print(soup.div.string)  # get div text
print(soup.div.text)  # same

print(soup.strong.string)  # get strong including comments
# print(type(soup.strong.string))
if type(soup.strong.string) == Comment:
    print(soup.strong.string)  # get rid of comments
    print(soup.strong.prettify())

else:
    print(soup.strong.text)

print("-----------------------")
print(soup.find_all('title'))
print(soup.find_all(id='title'))
print(soup.find_all(class_=''))
print(soup.find_all("div", attrs={'': ''}))

print("-----------------------")
print(soup.select('title'))
print(soup.select('#title'))
print(soup.select('.info'))

print(soup.select('div span'))  # same
print(soup.select('div > span'))

print(soup.select('div')[1].select('span'))

print(soup.select('title')[0].text)