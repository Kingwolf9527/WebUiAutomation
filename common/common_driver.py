# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/7/14 4:15

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import os
import threading
from selenium import webdriver
from common.common_log import CommonLog
from common.common_file_path import base_config_path
from common.common_config_yaml import CommonYaml

logger = CommonLog.get_logger()

class CommonDriver(object):

    _driver = None
    # 处理多线程会出现的单例模式问题
    _driver_lock = threading.Lock()

    @classmethod
    def get_driver(cls):
        """
        浏览器类型：谷歌，edge，火狐或者其他
        @return:
        """
        # 使用脚本开启浏览器的debug模式，调试时可以注释
        # os.popen(r"G:\selenium_debug.bat")-
        
        browser = CommonYaml(base_config_path).read_yaml()['browser_type']
        # 外层校验是为了避免单例已产生后，线程还要拿锁，浪费锁资源
        if cls._driver is None:
            with cls._driver_lock:
                # 内层校验是单例逻辑的条件判断，必须放在锁内，是为了避免线程在等锁的过程中单例已产生
                if cls._driver is None:
                    # cls.__driver = getattr(webdriver, browser)(executable_path=chrome_driver_path)
                    if browser.lower() == "firefox":
                        logger.info(f"-------当前浏览器是：{browser}-------")
                        cls._driver = webdriver.Firefox()
                    elif browser.lower() == "edge":
                        logger.info(f"-------当前浏览器是：{browser}-------")
                        cls._driver = webdriver.Edge()
                    elif browser.lower() == "chrome":
                        logger.info(f"-------当前浏览器是：{browser}-------")
                        # debug调试使用
                        # options = webdriver.ChromeOptions()
                        # options.debugger_address = "127.0.0.1:9222"
                        # cls._driver = webdriver.Chrome(options=options)
                        cls._driver = webdriver.Chrome()
                    else:
                        logger.error(f"-------暂时不支持当前浏览器：{browser}，请更换一款浏览器！(暂时支持Chrome，Firefox，edge)-------")
                        raise KeyError(f"暂时不支持当前浏览器：{browser}，请更换一款浏览器！(暂时支持Chrome，Firefox，edge)")
                
                return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            # 退出后，重新置空_driver
            logger.info(f"-------重新置空driver-------")
            cls._driver = None
            
if __name__ == '__main__':
    d = CommonDriver()
    dd = d.get_driver()
    dd.get("https://douyu.com")
