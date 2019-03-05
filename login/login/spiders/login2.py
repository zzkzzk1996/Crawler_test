# -*- coding: utf-8 -*-
import scrapy


class Login2Spider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['sxt.cn']

    # start_urls = ['https://www.sxt.cn/index/user.html']
    def start_requests(self):
        cookie_str = 'zg_did=%7B%22did%22%3A%20%221694b869914875-0bf1c6d90ccd1d-36657105-13c680-1694b869915910%22%7D; UM_distinctid=1694b869dde4b1-04bdbad135116e-36657105-13c680-1694b869ddf763; PHPSESSID=tg6q1ra7taeftcmd16t31koqm4; 53gid2=11305488417012; 53gid0=11305488417012; 53gid1=11305488417012; 53revisit=1551750311996; 53kf_72085067_from_host=www.sxt.cn; 53kf_72085067_land_page=https%253A%252F%252Fwww.sxt.cn%252F; kf_72085067_land_page_ok=1; CNZZDATA1261969808=1657423921-1551750306-%7C1551749325; visitor_type=old; 53kf_72085067_keyword=https%3A%2F%2Fwww.sxt.cn%2Findex%2Flogin%2Flogin.html; zg_c1e08f0fa5e3446d854919ffa754d07f=%7B%22sid%22%3A%201551750306075%2C%22updated%22%3A%201551751202366%2C%22info%22%3A%201551750306080%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E8%AF%B8%E8%91%9Bio%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.sxt.cn%2F%22%7D'
        cookies = {}
        for cookie in cookie_str.split(';'):
            key, value = cookie.split('=', 1)
            cookies[key.strip()] = value.strip()
        yield scrapy.Request('https://www.sxt.cn/index/user.html', cookies=cookies, callback=self.parse)

    def parse(self, response):
        print(response.text)
