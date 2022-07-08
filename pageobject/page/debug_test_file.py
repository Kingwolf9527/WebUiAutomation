# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/6/26 5:50
#   @File      :    debug_test_file.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import time
from selenium.webdriver.common.by import By
from pageobject.page.tpshop_login_page import TpshopLoginPage

class Debug_(TpshopLoginPage):
    
    # 悬停定位进入地址管理
    account_setting = (By.XPATH, '//div[@class="u-dt"]/span')
    shipping_address = (By.LINK_TEXT, "收货地址")
    # 已经存在的地址数量
    exists_address_num = (By.XPATH, '//p[@class="gp_num2"]/em[1]')
    # 新增地址
    add_address_link = (By.LINK_TEXT, "增加新地址")
    consignee_ = (By.NAME, "consignee")
    phone = (By.NAME, "mobile")
    province = (By.NAME, "province")
    city = (By.NAME, "city")
    district = (By.NAME, "district")
    town = (By.NAME, "twon")
    detail_address_ = (By.NAME, "address")
    zipcode_ = (By.NAME, "zipcode")
    # 保存
    save_button = (By.ID, "address_submit")
    

    def add_address_personal(self):
        
        # 悬停进入地址管理
        self.mouse().move_to_element(self.find_element_highlight(Debug_.account_setting)).perform()
        self.click(Debug_.shipping_address)
        # 先获取已经保存的地址数量
        self.add_before = int(self.get_element_text(self.find_element_highlight(Debug_.exists_address_num)))
        # 新增地址
        self.click(Debug_.add_address_link)
        self.input(Debug_.consignee_, 'king2')
        self.input(Debug_.phone, '13822272222')
        # 下拉框处理
        self.select_box(Debug_.province).select_by_index(19)
        time.sleep(2)
        self.select_box(Debug_.city).select_by_index(4)
        time.sleep(2)
        self.select_box(Debug_.district).select_by_index(2)
        time.sleep(2)
        self.select_box(Debug_.town).select_by_index(3)
        time.sleep(2)
        # 详细地址以及邮编
        self.input(Debug_.detail_address_, '吉大吉利大道7777777号')
        self.input(Debug_.zipcode_, '519000')
        self.click(Debug_.save_button)
        time.sleep(3)
        
if __name__ == '__main__':
    pass