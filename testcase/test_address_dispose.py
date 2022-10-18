# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/6/14 3:27
#   @File      :    test_address_dispose.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import pytest
import allure
from pageobject.page.address_dispose_page import Address
from pageobject.page.tpshop_login_page import TpshopLoginPage
from common.common_config_yaml import CommonYaml
from common.common_file_path import base_yaml_path
from common.common_log import CommonLog

logger = CommonLog().get_logger()


@allure.feature("前台个人中心的地址管理")
class TestAddressDispose(object):
    
    @allure.story("收货地址的增删改查")
    @pytest.mark.parametrize("account_info", CommonYaml(base_yaml_path.joinpath("login_data.yaml")).read_yaml())
    @pytest.mark.parametrize("address_infos", CommonYaml(base_yaml_path.joinpath("change_address.yaml")).read_yaml())
    def test_address_add(self, account_info, address_infos, get_driver):
        """
        处理收货地址
        @param account_info:
        @param address_infos:
        @param get_driver:
        @return:
        """
        logger.info(f"--------正在执行登录操作！ --------")
        d = TpshopLoginPage(get_driver)
        d.tpshop_login(**account_info)
        assert d.is_displayed(account_info['login_base']['exchanges']) == True
        logger.info(f"--------登录成功！ --------")
        
        logger.info(f"--------正在执行新增收货地址操作！ --------")
        dd = Address(get_driver)
        dd.add_address(**address_infos)
        add_after = int(dd.get_element_text(dd.find_element_highlight(address_infos["address_dispose"]["exists_address_num"])))
        assert add_after == dd.address_before_num + 1
        logger.info(f"-------- 新增的地址完毕！ --------")
        logger.info(f"-------- 最新成功保存的地址数量为：{add_after}条 --------")

        logger.info(f"--------正在执行删除收货地址操作！ --------")
        dd.delete_address(**address_infos)
        logger.info(f"--------删除的收货地址联系人为：{dd.delete_address_consignee_name} --------")
        delete_after = int(dd.get_element_text(dd.find_element_highlight(address_infos["address_dispose"]["exists_address_num"])))
        assert delete_after == add_after - 1
        logger.info(f"----------删除地址完毕！ --------")
        logger.info(f"-------- 最新成功保存的地址数量为：{delete_after}条 --------")


if __name__ == '__main__':
    pytest.main()
