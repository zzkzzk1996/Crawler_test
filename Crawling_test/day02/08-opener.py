from urllib.request import build_opener
from urllib.request import Request
from fake_useragent import UserAgent
from urllib.request import HTTPHandler

url = "http://www.baidu.com"
headers = {
    "User-Agent": UserAgent().chrome
}

# urlopen is enveloped
request = Request(url, headers=headers)
handler = HTTPHandler()
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
