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
from pageobject.page.tpshop_login_page import TpshopLoginPage
from common.common_config_yaml import CommonYaml
from common.common_file_path import  base_yaml_path
from common.common_log import CommonLog

logger = CommonLog().get_logger()

@allure.feature("冒烟BVT测试")
class TestBvt(object):
    
    @allure.story("登录-搜索产品-添加购物车-购物车结算-使用余额支付-提交订单")
    @pytest.mark.parametrize("account_info", CommonYaml(base_yaml_path / 'login_data.yaml').read_yaml())
    @pytest.mark.parametrize("bvt_infos", CommonYaml(base_yaml_path.joinpath('bvt.yaml')).read_yaml())
    def test_bvt(self, account_info, bvt_infos, get_driver):
        """
        BVT测试
        @param account_info:
        @param bvt_infos:
        @param get_driver:
        @return:
        """
        logger.info(f"--------正在执行冒烟测试操作！ --------")
        
        logger.info(f"--------正在执行登录操作！ --------")
        d = TpshopLoginPage(get_driver)
        d.tpshop_login(**account_info)
        assert d.is_displayed(account_info['login_base']['exchanges']) == True
        logger.info(f"--------登录成功！ --------")
        
        logger.info(f"-------- 正在执行搜索产品-添加购物车-购物车结算-使用余额支付-提交订单测试！--------")
        dd = Bvt(get_driver)
        dd.bvt_test(**bvt_infos)
        assert dd.is_displayed(bvt_infos["bvt_base"]["deliver"]) == True
        logger.info(f'-------- 当前页面的‘待发货’元素是否显示：{dd.is_displayed(bvt_infos["bvt_base"]["deliver"])} --------')
        logger.info(f"-------- 冒烟测试成功！ --------")

if __name__ == '__main__':
    pytest.main()