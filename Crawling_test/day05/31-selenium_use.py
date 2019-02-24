from selenium import webdriver


def firefox_text():
    fox = webdriver.Firefox()

    fox.get("https://www.bing.com/?mkt=zh-CN")

    fox.find_element_by_id("sb_form_q").send_keys("python")

    fox.find_element_by_id("sb_form_go").click()

    fox.quit()


def chrome_headless():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome = webdriver.Chrome(chrome_options=options)
    chrome.get("http://www.baidu.com")
    html = chrome.page_source
    print(html)


if __name__ == '__main__':
    chrome_headless()
