from urllib.request import urlopen

url = "https://www.baidu.com"
# send request
response = urlopen(url)
# get info
info = response.read()
# print info
print(info.decode())

# print http code
print(response.getcode())
# print real url
print(response.geturl())
# print head info
print(response.info())

