from urllib.request import Request, urlopen
from urllib.parse import quote
from urllib.parse import urlencode

args ={
    "wd": "尚学堂"
}

# url = "http://www.baidu.com/s?wd={}".format((quote("尚学堂")))
url = "http://www.baidu.com/s?wd={}".format(urlencode(args))


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())
