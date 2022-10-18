# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/6/14 0:08
#   @File      :    address_dispose_page.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import time
from ..base.base_handle import BaseHandle

class Address(BaseHandle):
    
    def add_address(self, **kwargs):
        """
        处理收货地址
        @param kwargs:
        @return:
        """
        # 悬停进入地址管理
        self.mouse().move_to_element(self.find_element_highlight(kwargs["address_dispose"]["account_setting"])).perform()
        self.click(kwargs["address_dispose"]["shipping_address"])
        # 先获取已经保存的地址数量
        self.address_before_num = int(self.get_element_text(self.find_element_highlight(kwargs["address_dispose"]["exists_address_num"])))
        # 新增地址
        self.click(kwargs["address_dispose"]["add_address_link"])
        self.input(kwargs["address_dispose"]["consignee_"], kwargs["address_dispose"]["consinee_name"])
        self.input(kwargs["address_dispose"]["phone"], kwargs["address_dispose"]["phone_num"])
        # 下拉框处理
        self.select_box(kwargs["address_dispose"]["province"]).select_by_visible_text(kwargs["address_dispose"]["provice_name"])
        time.sleep(2)
        self.select_box(kwargs["address_dispose"]["city"]).select_by_visible_text(kwargs["address_dispose"]["city_name"])
        time.sleep(2)
        self.select_box(kwargs["address_dispose"]["district"]).select_by_visible_text(kwargs["address_dispose"]["district_name"])
        time.sleep(2)
        self.select_box(kwargs["address_dispose"]["town"]).select_by_visible_text(kwargs["address_dispose"]["town_name"])
        time.sleep(2)
        # 详细地址以及邮编
        self.input(kwargs["address_dispose"]["detail_address_"], kwargs["address_dispose"]["detail_address_name"])
        self.input(kwargs["address_dispose"]["zipcode_"], kwargs["address_dispose"]["zipcode_num"])
        self.click(kwargs["address_dispose"]["save_button"])
        time.sleep(3)
        
    def delete_address(self, **kwargs):
        """
        删除收货地址
        @param kwargs:
        @return:
        """
        # 删除地址对应的联系人
        self.delete_address_consignee_name = self.get_element_text(self.find_element_highlight(kwargs["address_dispose"]["delete_address_consignee_name"]))
        # 删除地址
        self.click(kwargs["address_dispose"]["delete_address_"])
        time.sleep(3)
