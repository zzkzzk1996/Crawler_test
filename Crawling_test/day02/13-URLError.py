from urllib.request import urlopen, Request
from fake_useragent import UserAgent
from urllib.error import URLError

url = "https://www.sxt22.cn/index/login/login123"

headers = {
    "User-Agent": UserAgent().chrome
}

try:
    request = Request(url, headers=headers)
    response = urlopen(request)
    print(response.read().decode())
except URLError as e:
    if e.args == ():
        print(e.code)
    else:
        print(e.args[0].errno)

print("Finished")
