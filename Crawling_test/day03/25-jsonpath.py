from jsonpath import jsonpath as jp
import requests
from fake_useragent import UserAgent
import json


url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": UserAgent().random
}

response = requests.get(url, headers=headers)
names = jp(json.loads(response.text), '$..name') # caution to $$$$$$$$$$$$$$$$$$$
codes = jp(response.json(), '$..code')
print(names)
print(codes)