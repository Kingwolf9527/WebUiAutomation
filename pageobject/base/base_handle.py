# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/9/16 2:35

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
from pathlib import Path
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as AC
from common.common_file_path import image_dir
from common.common_log import CommonLog
from ..base.base_view import BaseView
from common.common_log import CommonLog

logger = CommonLog().get_logger()


class BaseHandle(BaseView):
    
    
    def back(self):
        """
        页面后退
        @return:
        """
        self.driver.back()
        
    def forword(self):
        """
        页面前进
        @return:
        """
        self.driver.forword()
        
    def refresh(self):
        """
        当前页面刷新
        @return:
        """
        self.driver.refresh()
        
    def open(self, url):
        """
        打开指定URL
        @param url:
        @return:
        """
        logger.info(f"当前操作为：open，打开的URL为：{url}")
        self.driver.get(url)

    def quit(self):
        """
        退出窗口
        @return:
        """
        logger.info("当前的操作为：quit")
        self.driver.quit()

    def maximize(self):
        """
        窗口最大化
        @return:
        """
        logger.info("当前的操作为：maximize")
        self.driver.maximize_window()

    def click(self, loc):
        """
        元素点击操作
        @param loc:
        @return:
        """
        logger.info(f"当前的操作为：click")
        self.find_element_highlight(loc).click()

    def input(self, loc, value):
        """
        输入内容
        @param loc:
        @param value:
        @return:
        """
        logger.info(f"当前的操作为：input，输入的值为：{value}")
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
        if isinstance(element, list):
            logger.info(f"当前的操作为：get_location，获取的元素坐标为：{self.find_element_highlight(element).location}")
            return self.find_element_highlight(element).location
        logger.info(f"当前的操作为：get_location，获取的元素坐标为：{element.location}")
        return element.location

    def get_size(self, element):
        """
        或者元素的大小，返回值类似：{"width":xxx, "height":xxxxx}
        @param element:
        @return:
        """
        if isinstance(element, list):
            logger.info(f"当前的操作为：get_size，获取的元素坐标为：{self.find_element_highlight(element).size}")
            return self.find_element_highlight(element).size
        logger.info(f"当前的操作为：get_size，获取的元素坐标为：{element.size}")
        return element.size

    def get_page_source(self):
        """
        获取页面源代码
        @return:
        """
        logger.info("当前操作为：get_page_source，获取当前页面的源代码！")
        return self.driver.page_source

    def get_attribute(self, element, name):
        """
        获取指定名称的属性值
        @param element:
        @param name:
        @return:
        """
        if isinstance(element, list):
            logger.info(f"当前的操作为：get_attribute，获取的指定属性值为：{self.find_element_highlight(element).get_attribute(name)}")
            return self.find_element_highlight(element).get_attribute(name)
        logger.info(f"当前的操作为：get_attribute，获取的指定属性值为：{element.get_attribute(name)}")
        return element.get_attribute(name)

    def get_element_text(self, element):
        """
        获取元素的文本
        @param element:
        @return:
        """
        if isinstance(element, list):
            logger.info(f"当前的操作为：get_element_text，获取的元素的文本值为：{self.find_element_highlight(element).text}")
            return self.find_element_highlight(element).text
        logger.info(f"当前的操作为：get_element_text，获取的元素的文本值为：{element.text}")
        return element.text

    def get_current_url(self):
        """
        获取当前页面URL
        @return:
        """
        logger.info(f"当前操作为：get_current_url，获取到当前URL为：{self.driver.current_url}")
        return self.driver.current_url

    def get_current_window(self):
        """
        获取当前页面句柄
        @return:
        """
        logger.info(f"当前操作为：get_current_window，获取到当前句柄为：{self.driver.current_window_handle}")
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
        logger.info(f"当前操作为：window_into，切换的句柄为：{window_name}")
        self.driver.switch_to.window(window_name)
        
    def switchto_alert(self):
        """
        切换alert弹窗
        @return:
        """
        self.driver.switch_to.alert

    def iframe_into(self, iframe):
        """
        切换进入iframe
        @param iframe:  iframe定位为name，id时，类型为str
                        xpath，tag_name等定位到的iframe元素时，类型为element(元素)
        @return:
        """
        if isinstance(iframe, str):
            self.driver.switch_to.frame(iframe)
            logger.info(f"当前操作为：iframe_into，页面进行iframe切换，当前iframe名称或者id为：{iframe}")
        else:
            logger.info(f"当前操作为：iframe_into，页面进行iframe切换，当前iframe元素为：{self.find_element_highlight(iframe)}")
            self.driver.switch_to.frame(self.find_element_highlight(iframe))

    def iframe_out(self):
        """
        退出当前iframe，回到top层
        @return:
        """
        logger.info(f"当前操作为：iframe_out，页面退出iframe，返回top层！")
        self.driver.switch_to.default_content()

    def select_box(self, loc):
        """
        下拉框处理
        @param loc:
        @return:
        """
        logger.info("当前操作为：select_box，select标签下的处理！")
        return Select(self.find_element_highlight(loc))

    def mouse(self):
        """
        鼠标处理
        @return:
        """
        logger.info("当前操作为：mouse，鼠标相关操作的处理！")
        return AC(self.driver)

    def is_selected(self, element):
        """
        判断元素是否被选中(结果是布尔值)
        @param element:
        @return:
        """
        if isinstance(element, list):
            logger.info(f"当前操作为：is_selected，当前元素：{self.find_element_highlight(element)}已经被选中！")
            return self.find_element_highlight(element).is_selected()
        logger.info(f"当前操作为：is_selected，当前元素：{element}已经被选中！")
        return element.is_selected()

    def is_displayed(self, element):
        """
        判断元素是否显示(结果是布尔值)
        @param element:
        @return:
        """
        if isinstance(element, list):
            logger.info(f"当前操作为：is_displayed，当前元素：{self.find_element_highlight(element)}已经显示！")
            return self.find_element_highlight(element).is_displayed()
        logger.info(f"当前操作为：is_displayed，当前元素：{element}已经显示！")
        return element.is_displayed()

    def is_enabled(self, element):
        """
        判断元素是否被使用(结果是布尔值)
        @param element:
        @return:
        """
        if isinstance(element, list):
            logger.info(f"当前操作为：is_enabled，当前元素：{self.find_element_highlight(element)}可以被使用！")
            return self.find_element_highlight(element).is_enabled()
        logger.info(f"当前操作为：is_enabled，当前元素：{element}可以被使用！")
        return element.is_enabled()
    
    def scroll_buttom(self):
        """
        滚动条拖到页面底部
        @return:
        """
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        
    def scroll_top(self):
        """
        滚动条拖到页面顶部
        @return:
        """
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        
    def scroll_target(self, element):
        """
        滚动条拖动到可见的元素去
        @param element:
        @return:
        """
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, element)

    def save_screenshot(self, img_name):
        """
        保存截图
        @param img_name: 截图命名规范 页面名称_页面行为_时间.png
        @return:
        """
        # 格式化处理时间
        now_time = time.strftime("%Y-%m-%d-%H_%M_%S")
        # 判断截图文件夹是否存在
        exists_dir = Path.exists(image_dir)
        if not exists_dir:
            try:
                Path.mkdir(image_dir)
            except FileExistsError:
                raise FileNotFoundError("------- 文件找不到！ -------")
        # 截图保存路径
        save_image_path = image_dir.joinpath(f"{img_name}_{now_time}.png")
        try:
            self.driver.get_screenshot_as_file(save_image_path)
            logger.info(f'-------截图当前网页成功并存储在：{save_image_path}-------')
        except:
            logger.error(f"------- 截图当前网页失败！ -------")



if __name__ == '__main__':
    d = BaseView()
    d.open("https://tieba.baidu.com/")
