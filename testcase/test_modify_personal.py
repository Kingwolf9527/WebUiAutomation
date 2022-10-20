# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/10/19 4:45
#   @File      :    test_modify_personal.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import pytest
import allure
from pageobject.page.modify_personal import ModifyPersonal
from pageobject.page.tpshop_login_page import TpshopLoginPage
from common.common_config_yaml import CommonYaml
from common.common_file_path import base_yaml_path
from common.common_log import CommonLog

logger = CommonLog().get_logger()


@allure.feature("个人信息页面处理")
class TestModifyPersonal(object):
    
    @allure.story("修改'个人页面'相关信息")
    @pytest.mark.parametrize("account_info", CommonYaml(base_yaml_path.joinpath("login_data.yaml")).read_yaml())
    @pytest.mark.parametrize("personal_infos", CommonYaml(base_yaml_path.joinpath("modify_person_info.yaml")).read_yaml())
    def test_modify_personal(self, account_info, personal_infos, get_driver):
        """
        修改"个人信息"页面的相关信息
        @param account_info:
        @param personal_infos:
        @param get_driver:
        @return:
        """
        logger.info(f"--------正在执行登录操作！ --------")
        d = TpshopLoginPage(get_driver)
        d.tpshop_login(**account_info)
        assert d.is_displayed(account_info['login_base']['exchanges']) == True
        logger.info(f"--------登录成功！ --------")
        
        logger.info(f"--------正在执行修改个人信息操作！ --------")
        dd = ModifyPersonal(get_driver)
        dd.modify_info(**personal_infos)
        assert dd.success_flag == dd.forecast_text
        logger.info(f"--------修改个人信息成功！ --------")


        