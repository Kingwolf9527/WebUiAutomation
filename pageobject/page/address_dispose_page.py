# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/6/14 0:08
#   @File      :    address_dispose_page.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import time
from selenium.webdriver.common.by import By
from pageobject.page.tpshop_login_page import TpshopLoginPage

class Address(TpshopLoginPage):
    
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
    
    # 删除地址
    delete_address_ = (By.XPATH, '//ul[@class="add_conta"][1]//a[@class="address_delete co_blue"]')
    
    def add_address(self, username, password, verify_code, consignee, phone_num, detail_address, zipcode):
        """
        新增地址
        @param username:
        @param password:
        @param verify_code:
        @param consignee:
        @param phone_num:
        @param detail_address:
        @param zipcode:
        @return:
        """
        # 登录
        self.tpshop_login(username, password, verify_code)
        # 悬停进入地址管理
        self.mouse().move_to_element(self.find_element_highlight(Address.account_setting)).perform()
        self.click(Address.shipping_address)
        # 先获取已经保存的地址数量
        self.add_before = int(self.get_element_text(self.find_element_highlight(Address.exists_address_num)))
        # 新增地址
        self.click(Address.add_address_link)
        self.input(Address.consignee_, consignee)
        self.input(Address.phone, phone_num)
        # 下拉框处理
        self.select_box(Address.province).select_by_index(19)
        time.sleep(2)
        self.select_box(Address.city).select_by_index(4)
        time.sleep(2)
        self.select_box(Address.district).select_by_index(2)
        time.sleep(2)
        self.select_box(Address.town).select_by_index(3)
        time.sleep(2)
        # 详细地址以及邮编
        self.input(Address.detail_address_, detail_address)
        self.input(Address.zipcode_, zipcode)
        self.click(Address.save_button)
        time.sleep(3)
        # 退出，重置driver
        self.quit()
        
    
    def delete_address(self, username, password, verify_code):
        """
        删除地址
        @param username:
        @param password:
        @param verify_code:
        @return:
        """
        # 登录
        self.tpshop_login(username, password, verify_code)
        # 悬停进入地址管理
        self.mouse().move_to_element(self.find_element_highlight(Address.account_setting)).perform()
        self.click(Address.shipping_address)
        # 先获取已经保存的地址数量
        self.delete_before = int(self.get_element_text(self.find_element_highlight(Address.exists_address_num)))
        self.click(Address.delete_address_)
        time.sleep(3)
        # 退出，重置driver
        self.quit()