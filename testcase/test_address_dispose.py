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
from common.common_config_yaml import CommonYaml
from common.common_file_path import foreground_infos
from common.common_log import CommonLog

logger = CommonLog().get_logger()


@allure.feature("前台个人中心的地址管理")
class TestAddressDispose(object):
    
    @allure.story("新增地址")
    @pytest.mark.parametrize("infos", CommonYaml(foreground_infos).read_yaml())
    def test_address_add(self, infos, get_driver):
        """
        新增地址
        @param infos:
        @return:
        """
        logger.info(f"--------正在执行新增收货地址操作！ --------")
        dd = Address(get_driver)
        dd.add_address(username=infos["username"], password=infos["password"], verify_code="2222",
                       consignee=infos["consignee"], phone_num=infos["phone_num"],
                       detail_address=infos["detail_address"],
                       zipcode=infos["zipcode"])
        add_after = int(dd.get_element_text(dd.find_element_highlight(dd.exists_address_num)))
        assert add_after == dd.add_before + 1
        logger.info(f"-------- 新增的地址完毕！ --------")
        logger.info(f"-------- 最新成功保存的地址数量为：{add_after}条 --------")
    
    @allure.story("删除地址")
    @pytest.mark.parametrize("infos", CommonYaml(foreground_infos).read_yaml())
    def test_address_delete(self, infos, get_driver):
        """
        删除地址
        @param infos:
        @param get_driver:
        @return:
        """
        logger.info(f"--------正在执行删除收货地址操作！ --------")
        dd = Address(get_driver)
        dd.delete_address(username=infos["username"], password=infos["password"], verify_code="2222")
        delete_after = int(dd.get_element_text(dd.exists_address_num))
        assert delete_after == dd.delete_before - 1
        logger.info(f"-------- 删除地址完毕！ --------")
        logger.info(f"-------- 最新保存的地址数量为：{delete_after}条 --------")


if __name__ == '__main__':
    pytest.main()
