# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/8/10 18:00

import sys
from selenium.webdriver.support.wait import WebDriverWait
from common.common_driver import CommonDriver

sys.path.append("..")
sys.path.append(r"F:\WebUiAutomation")

class BaseView(object):

    def __init__(self, browser):
        self.driver = CommonDriver().get_driver(browser)

    def find_element(self, loc, timeout=30, poll_frequency=0.5):
        """
        base元素查询
        @param loc: 格式为元祖，类似：login_link = (By.Partiallink, "登录")
        @param timeout:
        @param poll_frequency:
        @return:
        """
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=1000, poll_frequency=0.5):
        """
        获取一组元素，结果为list
        @param loc: 格式为元祖，类似：login_link = (By.Partiallink, "登录")
        @param timeout:
        @param poll_frequency:
        @return:
        """
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency).until(lambda x: x.find_elements(*loc))

    def find_element_highlight(self, loc):
        """
        高亮显示定位的元素(背景黄色，边框红色，大小设置为3px)
        @param loc:
        @return:
        """
        element = self.find_element(loc)
        highlight_style = "background: yellow;  border: 3px solid red;"
        js = "arguments[0].setAttribute('style', arguments[1]);"
        # 元素样式属性修改
        self.driver.execute_script(js, element, highlight_style)
        return element
