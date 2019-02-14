import requests
from fake_useragent import UserAgent
import re

url = "https://www.qiushibaike.com/text/page/1/"
headers = {
    "User-Agent": UserAgent().random
}

# form request
response = requests.get(url, headers=headers)
info = response.text
print(info)
# contents = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>', info)
# print(contents)
#
# with open('Contents.txt', 'w', encoding='utf-8') as f:
#     for info in contents:
#         f.write(info+"\n\n\n")
