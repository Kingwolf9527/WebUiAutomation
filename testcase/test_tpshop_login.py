# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/6/13 4:13
#   @File      :    test_tpshop_login.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import pytest
import allure
from pageobject.page.tpshop_login_page import TpshopLoginPage
from common.common_config_yaml import CommonYaml
from common.common_file_path import foreground_infos
from common.common_log import CommonLog

logger = CommonLog().get_logger()

@allure.feature("Tpshop项目的登录测试")
class TestTpshopLogin(object):
    
    @allure.story("验证登录功能")
    @pytest.mark.parametrize("account_info", CommonYaml(foreground_infos).read_yaml())
    def test_tpshop_login(self, account_info, get_driver):
        """
        账号信息
        @param account_info:
        @param get_driver:
        @return:
        """
        logger.info(f"--------正在执行登录操作！ --------")
        dd = TpshopLoginPage(get_driver)
        dd.tpshop_login(account_info['username'], account_info['password'], '2222')
        assert dd.is_displayed(dd.exchanges) == True
        logger.info(f"-------- 当前页面的‘交易中心’元素是否显示：{dd.is_displayed(dd.exchanges)} --------")
        assert dd.get_current_url() == dd.login_success_url
        logger.info(f"-------- 当前页面的URL为：{dd.get_current_url()} --------")
        logger.info(f"--------登录成功！ --------")



if __name__ == '__main__':
    pytest.main()