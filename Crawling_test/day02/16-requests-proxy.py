from fake_useragent import UserAgent
import requests

url = "http://httpbin.org/get"

proxies = {
    "http": "39.137.46.77:80"
}

headers = {
    "User-Agent": UserAgent().chrome
}

response = requests.get(url, headers=headers, proxies=proxies)
print(response.text)