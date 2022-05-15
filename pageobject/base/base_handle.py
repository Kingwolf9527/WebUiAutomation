# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/9/16 2:35

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as AC
from pageobject.base.base_view import BaseView


class BaseHandle(BaseView):

    def open(self, url):
        """
        打开指定URL
        @param url:
        @return:
        """
        self.driver.get(url)

    def maximize(self):
        """
        窗口最大化
        @return:
        """
        self.driver.maximize_window()

    def click(self, loc):
        """
        元素点击操作
        @param loc:
        @return:
        """
        self.find_element_highlight(loc).click()

    def input(self, loc, value):
        """
        输入内容
        @param loc:
        @param value:
        @return:
        """
        ele = self.find_element_highlight(loc)
        # 先清空
        ele.clear()
        # 再输入
        ele.send_keys(value)

    def get_location(self, element):
        """
        获取元素的坐标，返回值类似:{"x":xxx, "y":xxxxx}
        @param element:
        @return:
        """
        return element.location

    def get_size(self, element):
        """
        或者元素的大小，返回值类似：{"width":xxx, "height":xxxxx}
        @param element:
        @return:
        """
        return element.size

    def get_page_source(self):
        """
        获取页面源代码
        @return:
        """
        return self.driver.page_source

    def get_attribute(self, element, name):
        """
        获取指定名称的属性值
        @param element:
        @param name:
        @return:
        """
        return element.get_attribute(name)

    def get_element_text(self, element):
        """
        获取元素的文本
        @param element:
        @return:
        """
        return element.text

    def get_current_url(self):
        """
        获取当前页面URL
        @return:
        """
        return self.driver.current_url

    def get_current_window(self):
        """
        获取当前页面句柄
        @return:
        """
        return self.driver.current_window_handle

    def get_windows(self):
        """
        获取所有tab页句柄
        @return:
        """
        return self.driver.window_handles

    def window_into(self, window_name):
        """
        切换指定的句柄
        @param window_name:
        @return:
        """
        self.driver.switch_to.window(window_name)

    def iframe_into(self, iframe):
        """
        切换进入iframe
        @param iframe:  iframe类型可以为name，id，或者xpath，tag_name定位到的iframe元素
        @return:
        """
        self.driver.switch_to.frame(iframe)

    def iframe_out(self):
        """
        退出当前iframe，对到top层
        @return:
        """
        self.driver.switch_to.default_content()

    def select_box(self, loc):
        """
        下拉框处理
        @param loc:
        @return:
        """
        return Select(self.find_element_highlight(loc))

    def mouse(self):
        """
        鼠标处理
        @return:
        """
        return AC(self.driver)

    def is_selected(self, element):
        """
        判断元素是否被选中(结果是布尔值)
        @param element:
        @return:
        """
        return element.is_selected()

    def is_displayed(self, element):
        """
        判断元素是否显示(结果是布尔值)
        @param element:
        @return:
        """
        return element.is_displayed()

    def is_enabled(self, element):
        """
        判断元素是否被使用(结果是布尔值)
        @param element:
        @return:
        """
        return element.is_enabled()



if __name__ == '__main__':
    d = BaseHandle(browser="chrome")
    d.open("https://tieba.baidu.com/")