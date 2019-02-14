
from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, build_opener

# login
login_url = "https://www.sxt.cn/index/login/login"
headers = {
    "User-Agent": UserAgent().chrome
}
form_data = {
    "user": "17703181473",
    "password": "123456"
}
f_data = urlencode(form_data).encode()
request = Request(login_url, headers=headers, data=f_data)
handler = HTTPCookieProcessor()
opener = build_opener(handler)
# response = urlopen(request) ------- can't save cookie
response = opener.open(request)
print(response.read().decode())
#
# # AccessPage
# info_url = "http://www.sxt.cn/index/user.html"
# request = Request(info_url, headers=headers)
# response = opener.open(request)
# print(response.read().decode())
