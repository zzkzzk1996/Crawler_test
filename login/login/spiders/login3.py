# -*- coding: utf-8 -*-
import scrapy
import re


class Login3Spider(scrapy.Spider):
    name = 'login3'
    allowed_domains = ['ganji.com']
    start_urls = ['https://passport.ganji.com/login.php']

    def parse(self, response):
        hash_code = re.findall(r'"__hash__":"(.+)"', response.text)[0]
        img_url = 'https://passport.ganji.com/ajax.php?dir=captcha&module=login_captcha'
        yield scrapy.Request(img_url, callback=self.parse_info, meta={'hash_code': hash_code})

    def parse_info(self, response):
        hash_code = response.request.meta['hash_code']
        with open('vcode.jpg', 'wb') as f:
            f.write(response.body)

        vcode = input('Vcode: ')
        form_data = {
            "username": "17703181473",
            "password": "123456abcd",
            "setcookie": "0",
            "checkCode": vcode,
            "next": "/",
            "source": "passport",
            "__hash__": hash_code
        }
        login_url = 'https://passport.ganji.com/login.php'
        yield scrapy.FormRequest(login_url, callback=self.after_login, formdata=form_data)

    def after_login(self, response):
        print(response.text)
