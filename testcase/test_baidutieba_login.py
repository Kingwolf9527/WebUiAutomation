# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2022/4/14 23:34

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import pytest
import allure
from pageobject.page.login_page import LoginPage

@allure.feature("测试百度贴吧")
class TestTiebaLogin(object):
    
    @allure.story("测试百度贴吧自动登录以及自动签到功能")
    def test_login(self, get_driver):
        """
        @param get_driver:
        @return:
        """
        with allure.step("登录处理"):
            d = LoginPage(get_driver)
        with allure.step("签到处理"):
            d.go_sign("xxxx@qq.com", "xxxx")


if __name__ == '__main__':
    pytest.main()