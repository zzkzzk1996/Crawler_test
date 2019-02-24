import time  # 用来延时
from selenium import webdriver


# start webdriver and login
def login():
    chrome = webdriver.Chrome()  # choose Chrome as browser
    chrome.get('https://qzone.qq.com/')
    chrome.switch_to.frame('login_frame')
    chrome.find_element_by_id('switcher_plogin').click()
    chrome.find_element_by_name('u').clear()
    chrome.find_element_by_name('u').send_keys('1944212836')  # input username
    chrome.find_element_by_name('p').clear()
    chrome.find_element_by_name('p').send_keys('961006zzk')  # input password

    # chrome.execute_script("document.getElementById('login_button').parentNode.hidefocus=false;")

    # chrome.find_element_by_xpath('//*[@id="loginform"]/div[4]/a').click()
    chrome.find_element_by_id('login_button').click()  # click to login

    time.sleep(5)   # waiting for connecting

    btns = chrome.find_elements_by_css_selector('a.item.qz_like_btn_v3 ')  # css selector to locate where the thumb is

    # print(btns)
    for btn in btns:    # for loop to thumb every post
        # print(btn.text)
        btn.click()     # click thumb

    chrome.quit()   # finish and quit


if __name__ == '__main__':
    login()
