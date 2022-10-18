# - * - coding:utf-8
# __author__ : kingwolf
# create-time : 2022/4/12 22:33

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
from selenium.webdriver.common.by import By
from ..base.base_handle import BaseHandle


class Baidutieba(BaseHandle):


    # 页面操作
    def go_login(self, **kwargs):
        """
        登录操作
        @param kwargs: 
        @return: 
        """
        self.maximize()
        self.open(kwargs["baidu_tieba"]["login_url"])
        self.click(kwargs["baidu_tieba"]["login"])
        self.click(kwargs["baidu_tieba"]["switch_login"])
        self.input(kwargs["baidu_tieba"]["username"], kwargs["baidu_tieba"]["username_data"])
        self.input(kwargs["baidu_tieba"]["password"], kwargs["baidu_tieba"]["password_data"])
        self.click(kwargs["baidu_tieba"]["login_button"])

    def go_sign(self, **kwargs):
        """
        自动签到
        @param username:
        @param password:
        @return:
        """
        self.go_login(**kwargs)
        total_urls = []
        tieba_common = self.find_elements(kwargs["baidu_tieba"]["tieba_urls"])
        more_tieba = self.find_element_highlight(kwargs["baidu_tieba"]["more_tieba_check"])
        # 鼠标悬停才能获取其他贴吧地址
        self.mouse().move_to_element(more_tieba).perform()
        tieba_often = self.find_elements(kwargs["baidu_tieba"]["tieba_other_urls"])
        for common_url in (tieba_common + tieba_often):
            ever_tieba_url =  self.get_attribute(common_url, "href")
            total_urls.append(ever_tieba_url)

        for ever_tieba_url in total_urls:
            self.open(ever_tieba_url)
            self.click(kwargs["baidu_tieba"]["sign_button"])
        # # 退出，重置driver
        # self.quit()