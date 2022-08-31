# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/7/7 4:48
#   @File      :    base_view.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
from selenium.webdriver.support.wait import WebDriverWait
from common.common_log import CommonLog

logger = CommonLog().get_logger()


class BaseView(object):
    
    def __init__(self, driver):
        """
        初始化driver对象
        @param driver:-
        """
        self.driver = driver
    
    
    def find_element(self, loc, timeout=40, poll_frequency=0.5):
        """
        base元素查询
        @param loc: 格式为列表，类似：login_link = [xpath, '//a[@class="red"]']
        @param timeout:
        @param poll_frequency:
        @return:
        """
        logger.info(f"--------当前操作为：find_element，定位的方式为：{loc[0]}，定位的元素为：{loc[1]} --------")
        if loc[0].lower() == "xpath":
            return WebDriverWait(self.driver,
                                 timeout=timeout,
                                 poll_frequency=poll_frequency).until(lambda x: x.find_element_by_xpath(loc[1]))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x: x.find_element_by_css_selector(loc[1]))
    
    
    def find_elements(self, loc, timeout=1000, poll_frequency=0.5):
        """
        获取一组元素，结果为list
        @param loc: 格式为列表，类似：login_link = [xpath, '//a[@class="red"]']
        @param timeout:
        @param poll_frequency:
        @return:
        """
        logger.info(f"--------当前操作为：find_elementz，定位的方式为：{loc[0]}，定位的元素为：{loc[1]} --------")
        if loc[0].lower() == "xpath":
            return WebDriverWait(self.driver,
                                 timeout=timeout,
                                 poll_frequency=poll_frequency).until(lambda x: x.find_elements_by_xpath(loc[1]))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x: x.find_elements_by_css_selector(loc[1]))
    
    
    def find_element_highlight(self, loc):
        """
        高亮显示定位的元素(背景黄色，边框红色，大小设置为3px)
        @param loc:
        @return:
        """
        js = "arguments[0].setAttribute('style', arguments[1]);"
        element = self.find_element(loc)
        highlight_style_value = "background: yellow;  border: 3px solid red;"
        # 元素样式属性修改
        self.driver.execute_script(js, element, highlight_style_value)
        return element