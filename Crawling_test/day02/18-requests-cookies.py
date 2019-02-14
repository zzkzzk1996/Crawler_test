from fake_useragent import UserAgent
import requests

# open session for record the cookies
session = requests.Session()
headers = {
    "User-Agent": UserAgent().chrome
}

login_url = "https://www.sxt.cn/index/login/login"
params = {
    "user": "17703181473",
    "password": "123456"
}
response = session.post(login_url, headers=headers, data=params)
print(response.text)
info_url = "https://www.sxt.cn/index/user.html"
response = session.get(info_url, headers=headers)
print(response.text)
