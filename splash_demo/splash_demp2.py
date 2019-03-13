import requests
from fake_useragent import UserAgent
from urllib.parse import quote

url = "https://www.guazi.com/bj/buy/"
lua_script = '''
function main(splash, args)
    splash:go('{}')
    splash:wait(1)
    return splash:html()
end
'''.format(url)
splash_url = "http://0.0.0.0:8050/execute?lua_source={}".format(quote(lua_script))
response = requests.get(splash_url, headers={"User-Agent": UserAgent().random})
response.encoding = 'utf-8'
print(response.text)
