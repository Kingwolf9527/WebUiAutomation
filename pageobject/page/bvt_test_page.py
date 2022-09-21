# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/7/19 3:24
#   @File      :    bvt_test_page.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import time
from pageobject.base.base_handle import BaseHandle
from common.common_log import CommonLog

logger = CommonLog().get_logger()


class Bvt(BaseHandle):
    
    
    def bvt_test(self, **kwargs):
        """
        bvt测试page页面
        @param kwargs:
        @return:
        """
        # 再做其他操作
        self.input(kwargs["bvt_base"]["search_box"], kwargs["bvt_base"]["search_text"])
        self.click(kwargs["bvt_base"]["search_btn"])
        self.click(kwargs["bvt_base"]["add_to_cart"])
        self.click(kwargs["bvt_base"]["join_cart"])
        # 切换iframe
        self.iframe_into(kwargs["bvt_base"]["go_settlement_iframe"])
        self.click(kwargs["bvt_base"]["go_settlement"])
        # 退出iframe
        self.iframe_out()
        time.sleep(2)
        # 购物车页面以及获取总金额
        total_money = self.get_element_text(kwargs["bvt_base"]["total_fee"])
        # 字符串转为浮点数
        pay_num = float(total_money.split("￥")[-1])
        self.click(kwargs["bvt_base"]["pay_total"])
        # # 处理alert弹窗
        # self.switchto_alert()
        time.sleep(7)
        # 输入账户余额
        self.click(kwargs["bvt_base"]["use_balance"])
        time.sleep(1)
        self.input(kwargs["bvt_base"]["input_balance"], pay_num)
        time.sleep(2)
        # 输入支付密码
        self.input(kwargs["bvt_base"]["pay_pwd_ele"], kwargs["bvt_base"]["pay_pwd"])
        # 提交订单
        self.click(kwargs["bvt_base"]["summit_order"])
        time.sleep(3)


