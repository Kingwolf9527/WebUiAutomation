# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2022/4/14 23:34

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import pytest
import allure
from pageobject.page.tieba_login_page import Baidutieba
from common.common_config_yaml import CommonYaml
from common.common_file_path import base_yaml_path

@allure.feature("测试百度贴吧")
class TestTiebaLogin(object):
    
    @allure.story("测试百度贴吧自动登录以及自动签到功能")
    @pytest.mark.parametrize("tieba_info", CommonYaml(base_yaml_path.joinpath("tieba_sign.yaml")).read_yaml())
    def test_login(self, tieba_info, get_driver):
        """
        自动登录百度贴吧以及自动签到
        @param tieba_info:
        @param get_driver:
        @return:
        """
        with allure.step("登录处理"):
            d = Baidutieba(get_driver)
        with allure.step("签到处理"):
            d.go_sign(**tieba_info)

if __name__ == '__main__':
    pytest.main()