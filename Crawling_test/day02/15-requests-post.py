import requests
from fake_useragent import UserAgent

login_url = "https://www.sxt.cn/index/login/login"

headers = {
    "User-Agent": UserAgent().chrome
}

params = {
    "user": "17703181473",
    "password": "123456"
}

response = requests.post(login_url, headers=headers, data=params)
print(response.text)