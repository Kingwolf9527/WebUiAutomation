# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/6/13 4:01
#   @File      :    tpshop_login_page.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
from selenium.webdriver.common.by import By
from ..base.base_handle import BaseHandle

class TpshopLoginPage(BaseHandle):
    
    # 页面核心元素
    url = "http://www.kingwolf-book14.com:9090/"
    login_links = (By.LINK_TEXT, "登录")
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    verify_code = (By.NAME, "verify_code")
    login_button = (By.NAME, "sbtbutton")
    # 校验登录成功的标志
    login_success_url = "http://www.kingwolf-book14.com:9090/Home/User/index.html"
    exchanges = (By.XPATH, '//i[@class="account-acc1"]')
    
    # 页面操作
    def tpshop_login(self, username, password, verify_code):
        """
        tpshop执行登录操作
        @param username:
        @param password:
        @param verify_code: 采用万能验证码 2222
        @return:
        """
        self.maximize()
        self.open(TpshopLoginPage.url)
        self.click(TpshopLoginPage.login_links)
        self.input(TpshopLoginPage.username, username)
        self.input(TpshopLoginPage.password, password)
        self.input(TpshopLoginPage.verify_code, verify_code)
        self.click(TpshopLoginPage.login_button)
