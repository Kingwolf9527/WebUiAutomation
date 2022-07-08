# - * - coding:utf-8
# __author__ : kingwolf
# create-time : 2022/4/12 22:33

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
from selenium.webdriver.common.by import By
from ..base.base_handle import BaseHandle


class LoginPage(BaseHandle):

    # 页面元素
    login_url = "https://tieba.baidu.com"
    login = (By.LINK_TEXT, '登录')
    switch_login = (By.XPATH, '//div[@class="tang-pass-footerBar"]/p[@data-type="normal"]')
    username = (By.XPATH, '//input[@name="userName"]')
    password = (By.XPATH, '//input[@name="password"]')
    login_button = (By.XPATH, '//input[@id="TANGRAM__PSP_4__submit"]')
    tieba_urls = (By.XPATH, '//a[@class="u-f-item unsign"]')
    more_tieba_check = (By.XPATH, '//div[@id="moreforum"]/a')
    tieba_other_urls = (By.XPATH, '//a[@class="unsign"]')
    sign_button = (By.XPATH, '//a[contains(@class, "j_cansign")]')

    # 页面操作
    def go_login(self, username, password):
        """
        登录操作
        @param username:
        @param password:
        @return:
        """
        self.maximize()
        self.open(LoginPage.login_url)
        self.click(LoginPage.login)
        self.click(LoginPage.switch_login)
        self.input(LoginPage.username, username)
        self.input(LoginPage.password, password)
        self.click(LoginPage.login_button)

    def go_sign(self, username, password):
        """
        自动签到
        @param username:
        @param password:
        @return:
        """
        self.go_login(username, password)
        total_urls = []
        tieba_common = self.find_elements(LoginPage.tieba_urls)
        more_tieba = self.find_element_highlight(LoginPage.more_tieba_check)
        # 鼠标悬停才能获取其他贴吧地址
        self.mouse().move_to_element(more_tieba).perform()
        tieba_often = self.find_elements(LoginPage.tieba_other_urls)
        for common_url in (tieba_common + tieba_often):
            ever_tieba_url =  self.get_attribute(common_url, "href")
            total_urls.append(ever_tieba_url)

        for ever_tieba_url in total_urls:
            self.open(ever_tieba_url)
            self.click(LoginPage.sign_button)
        # # 退出，重置driver
        # self.quit()