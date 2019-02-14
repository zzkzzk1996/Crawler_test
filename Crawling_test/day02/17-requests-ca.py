from fake_useragent import UserAgent
import requests

url = "http://www.12306.cn/index"
headers = {
    "User-Agent": UserAgent().chrome
}

requests.packages.urllib3.disable_warnings()  # disable warnings for ssl
response = requests.get(url, verify=False, headers=headers)
response.encoding = "utf-8"  # if there are meaningless words use encoding to solve them
print(response.text)
