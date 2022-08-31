# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/6/13 4:01
#   @File      :    tpshop_login_page.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
from ..base.base_handle import BaseHandle

class TpshopLoginPage(BaseHandle):
    
    
    # 页面操作
    def tpshop_login(self, **kwargs):
        """
        tpshop执行登录操作
        @param kwargs:
        @return:
        """
        self.maximize()
        self.open(kwargs['login_base']['login_url'])
        self.click(kwargs['login_base']['login_links'])
        self.input(kwargs['login_base']['username'], kwargs['account_data']['username_base'])
        self.input(kwargs['login_base']['password'], kwargs['account_data']['password_base'])
        self.input(kwargs['login_base']['verify_code'], kwargs['account_data']['verify_code_base'])
        self.click(kwargs['login_base']['login_button'])

