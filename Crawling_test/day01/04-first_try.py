from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent


def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome
    }

    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read()


def save_html(filename, html_bytes):
    with open(filename, "wb") as f:
        f.write(html_bytes)


def main():
    content = input("what you wanna download: ")
    num = input("how many pages you wanna download: ")
    base_url = "http://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(num)):
        args = {
            "pn": pn * 50,
            "kw": content
        }
        args = urlencode(args)
        # print(base_url.format(args))
        filename = str(pn + 1) + ".html"
        print("Downloading" + filename)
        html_bytes = get_html(base_url.format(args))
        save_html(filename, html_bytes)


if __name__ == '__main__':
    main()
