# using fake_user_agents to camouflage the crawler itself

from urllib.request import urlopen
from urllib.request import Request
from random import choice

url = "https://www.baidu.com"

user_agents=[]

headers = {
    "User-Agent": choice(user_agents)
}
request = Request(url, headers=headers)
# print(request.get_header('User-agent'))  # really needs to pay attention to upper & lower case
response = urlopen(request)

info = response.read()

print(info.decode())