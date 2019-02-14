# from some websites which needs a certification authority with https request

from urllib.request import Request, urlopen
from fake_useragent import UserAgent

import ssl

url = "https://www.12306.cn/index/"

headers = {
    "User-Agent": UserAgent().chrome
}
request = Request(url, headers=headers)
# ignore certification authority
context = ssl._create_unverified_context()
response = urlopen(request, context=context)
info = response.read().decode()
print(info)
