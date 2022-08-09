# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/6/26 5:50
#   @File      :    debug_test_file.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
from selenium.webdriver.common.by import By
from pageobject.page.tpshop_login_page import TpshopLoginPage

class Debug_(TpshopLoginPage):
    
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
    # 这一步处理test环境支付弹窗
    # 商品总金额(例如：￥0.02)--处理数字
    total_price = (By.XPATH, '//div[@class="list"][1]/em')
    # 勾选使用账户余额
    use_balance = (By.XPATH, '//input[@id="user_money_checkbox"]')
    # 输入余额
    input_balance = (By.XPATH, '//input[@id="user_money"]')
    # 获取当前余额
    current_balance = (By.XPATH, '//p[@class="item"][2]//span')
    # 支付密码(6666aaaa)
    pay_pwd = (By.XPATH, '//p[@class="item"][4]//input')
    # 提交订单
    summit_order = (By.XPATH, '//button[@id="submit_order"]')
    
    def bvt_test(self):
        
        self.input(Debug_.search_box, Debug_.search_text)
        self.click(Debug_.search_btn)
        self.click(Debug_.add_to_cart)
        self.click(Debug_.join_cart)
        # 切换iframe
        self.iframe_into(Debug_.go_settlement_iframe)
        self.click(Debug_.go_settlement)
        # 退出iframe
        self.iframe_out()
        # 购物车页面
        self.click(Debug_.pay_total)
        # 处理alert弹窗
        self.switchto_alert().accept()
        # 获取总金额以及输入积分
        total_money = self.get_element_text(Debug_.total_price)
        pay_num = total_money.split("￥")[-1]
        self.click(Debug_.use_balance)
        self.input(Debug_.input_balance, pay_num)
        # 获取可用余额
        current_balan = self.get_element_text(Debug_.current_balance)
        # 输入支付密码
        self.input(Debug_.pay_pwd, "6666aaaa")
        # 提交订单
        self.click(Debug_.summit_order)
        
        
        
    
        
if __name__ == '__main__':
    pass