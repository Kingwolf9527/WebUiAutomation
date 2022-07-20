# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/7/19 3:24
#   @File      :    bvt_test_page.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import time
from selenium.webdriver.common.by import By
from pageobject.page.tpshop_login_page import TpshopLoginPage
from common.common_log import CommonLog

logger = CommonLog().get_logger()


class Bvt(TpshopLoginPage):
    
    search_box = (By.XPATH, '//input[@class="search_usercenter_text"]')
    search_btn = (By.XPATH, '//a[@class="search_usercenter_btn"]')
    search_text = "欧式陶瓷"
    add_to_cart = (By.XPATH, '//div[@class="p-btn"]/a')
    join_cart = (By.XPATH, '//a[@class="addcar buy_button"]')
    # 嵌套iframe
    go_settlement_iframe = (By.XPATH, '//div[@class="layui-layer-content"]/iframe')
    go_settlement = (By.XPATH, '//a[contains(@class, "ui-button-122")]')
    # 购物车页面结算
    pay_total = (By.XPATH, '//a[@class="paytotal"]')
    # 提前获取商品总金额(例如：￥0.02)--处理数字
    total_fee = (By.XPATH, '//div[contains(@class,"column t-sum sumpri")]/span')
    # 这一步处理test环境支付弹窗
    # 勾选使用账户余额
    use_balance = (By.XPATH, '//input[@id="user_money_checkbox"]')
    # 输入余额
    input_balance = (By.XPATH, '//input[@id="user_money"]')
    # 支付密码(6666aaaa)
    pay_pwd = (By.XPATH, '//p[@class="item"][4]//input')
    # 提交订单
    summit_order = (By.XPATH, '//button[@id="submit_order"]')
    # 代发货元素
    deliver = (By.XPATH, '//h1[@class="ddn2"]')
    
    def bvt_test(self, username, password, verify_code):
        """
        
        @param username:
        @param password:
        @param verify_code:
        @return:
        """
        # 先登錄
        self.tpshop_login(username, password, verify_code)
        # 再做其他操作
        self.input(Bvt.search_box, Bvt.search_text)
        self.click(Bvt.search_btn)
        self.click(Bvt.add_to_cart)
        self.click(Bvt.join_cart)
        # 切换iframe
        self.iframe_into(Bvt.go_settlement_iframe)
        self.click(Bvt.go_settlement)
        # 退出iframe
        self.iframe_out()
        time.sleep(2)
        # 购物车页面以及获取总金额
        total_money = self.get_element_text(Bvt.total_fee)
        # 字符串转为浮点数
        pay_num = float(total_money.split("￥")[-1])
        self.click(Bvt.pay_total)
        # 处理alert弹窗
        self.switchto_alert()
        time.sleep(7)
        # 输入积分
        self.click(Bvt.use_balance)
        time.sleep(1)
        self.input(Bvt.input_balance, pay_num)
        time.sleep(2)
        # 输入支付密码
        self.input(Bvt.pay_pwd, "6666aaaa")
        # 提交订单
        self.click(Bvt.summit_order)
        time.sleep(3)


