from urllib.request import Request
from urllib.request import ProxyHandler
from fake_useragent import UserAgent
from urllib.request import build_opener

url = "http://httpbin.org/get"

headers = {
    "User-Agent": UserAgent().chrome
}

request = Request(url, headers=headers)
# handler = ProxyHandler({"http": "username:password@ip:port"})
handler = ProxyHandler({"http": "39.137.46.77:80"})
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
