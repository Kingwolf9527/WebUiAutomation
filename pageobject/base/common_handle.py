# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/8/11 3:38

import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.common_config import CommonConfig
from common.common_file_path import image_dir
from common.common_log import CommonLog

logger = CommonLog.get_logger()

class CommonHandle(object):

    def __init__(self, driver):
        self.cf = CommonConfig()


    def get_element(self, selection, key):
        """
        处理不同的定位方法
        @param selection:   读取配置文件的元素定位
        @param key:
        @return:
        """
        target_element = self.cf.get_value(selection, key)
        # 区别元素定位方法跟其他元素
        if '>>>' in target_element:
            method = target_element.split('>>>')[0].strip()
            value = target_element.split('>>>')[1].strip()
            try:
                if method == "id":
                    return self.driver.base_find_element(By.ID, value)
                if method == "name":
                    return self.driver.base_find_element(By.NAME, value)
                if method == "tag name":
                    return self.driver.base_find_element(By.TAG_NAME, value)
                if method == "class name":
                    return self.driver.base_find_element(By.CLASS_NAME, value)
                if method == "link text":
                    return self.driver.base_find_element(By.LINK_TEXT, value)
                if method == "partial link text":
                    return self.driver.base_find_element(By.PARTIAL_LINK_TEXT, value)
                if method == "xpath":
                    return self.driver.base_find_element(By.XPATH, value)
                if method == "css selector":
                    return self.driver.base_find_element(By.CSS_SELECTOR, value)

            except NoSuchElementException:
                logger.error(f"------- 传入的定位方法有误,无法定位元素！请重新确认！ -------")
                raise NameError("传入的定位方法有误,无法定位元素！请重新确认！")
        # 处理非常规8种定位方式的元素
        elif len(target_element) > 0 and '>>>' not in target_element:
            logger.info(f"------- 读取到的非元素定位数据为：{target_element} -------")
            return target_element

        else:
            logger.error(f"------- The result is none！ -------")
            raise NameError('The result is none！')


    def get_current_url(self):
        """
        获取当前页面的URL
        @return:
        """
        return self.driver.current_url


    def get_title(self):
        """
        获取当前页面的title
        @return:
        """
        return self.driver.title


    def get_page_source(self):
        """
        获取当前页面源码
        @return:
        """
        return self.driver.page_source


    def get_elemnet_attribute(self, selection, key, attribute_name, img_name):
        """
        获取指定的属性值
        @param selection:
        @param key:
        @param attribute_name:
        @return:
        """
        element = self.get_element(selection, key)
        try:
            attribute_value = element.get_attribute(attribute_name)
        except:
            # 失败截图处理
            self.save_screenshot(img_name)
            logger.error(f"------- 获取元素的：{attribute_name}属性失败！ -------")
        else:
            logger.info(f"------- 属性值为：{attribute_value} -------")
            return attribute_value



    def save_screenshot(self, img_name):
        """
        保存截图
        @param img_name:         失败截图命名规范 页面名称_页面行为_时间.png
        @return:
        """
        # 格式化处理时间
        now_time = time.strftime("%Y-%m-%d-%H_%M_%S")
        # 判断截图文件夹是否存在
        existsDir = os.path.exists(image_dir)
        if not existsDir:
            try:
                os.makedirs(image_dir)
            except FileExistsError:
                raise FileNotFoundError("------- 文件找不到！ -------")
        # 截图保存路径
        save_image_path = os.path.join(image_dir, f"{img_name}_{now_time}.png")
        try:
            self.driver.get_screenshot_as_file(save_image_path)
            logger.info(f"-------截图当前网页成功并存储在：{save_image_path}-------")
        except:
            logger.error(f"------- 截图当前网页失败！ -------")


