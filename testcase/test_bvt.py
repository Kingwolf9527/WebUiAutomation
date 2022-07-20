# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/7/19 3:25
#   @File      :    test_bvt.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import pytest
import allure
from pageobject.page.bvt_test_page import Bvt
from common.common_config_yaml import CommonYaml
from common.common_file_path import foreground_infos
from common.common_log import CommonLog

logger = CommonLog().get_logger()

@allure.feature("冒烟BVT测试")
class TestBvt(object):
    
    @allure.story("登录-搜索产品-添加购物车-购物车结算-使用余额支付-提交订单")
    @pytest.mark.parametrize("infos", CommonYaml(foreground_infos).read_yaml())
    def test_bvt(self, infos, get_driver):
        """
        新增地址
        @param infos:
        @param get_driver:
        @return:
        """
        logger.info(f"--------正在执行冒烟試操作！ --------")
        dd = Bvt(get_driver)
        dd.bvt_test(username=infos["username"], password=infos["password"], verify_code="2222")
        assert dd.is_displayed(dd.deliver) is True
        logger.info(f"-------- 冒烟测试成功！！ --------")

if __name__ == '__main__':
    pytest.main()