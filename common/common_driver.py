# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/7/14 4:15

import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.edge.service import Service as ES
from selenium.webdriver.firefox.service import Service as FS
import threading
from common.common_file_path import chrome_driver_path, firefox_driver_path, edge_driver_path
from common.common_log import CommonLog
from common.common_config import CommonConfig

sys.path.append("..")
sys.path.append(r"F:\WebUiAutomation")
logger = CommonLog.get_logger()

class CommonDriver(object):

    __driver = None
    # 处理多线程会出现的单例模式问题
    __driver_lock = threading.Lock()

    @classmethod
    def get_driver(cls, browser):
        """
        浏览器类型：谷歌，edge，火狐或者其他
        @param browser:
        @return:
        """
        # 外层校验是为了避免单例已产生后，线程还要拿锁，浪费锁资源
        if cls.__driver is None:
            with cls.__driver_lock:
                # 内层校验是单例逻辑的条件判断，必须放在锁内，是为了避免线程在等锁的过程中单例已产生
                if cls.__driver is None:
                    # cls.__driver = getattr(webdriver, browser)(executable_path=chrome_driver_path)
                    if browser.lower() == "firefox":
                        logger.info(f"-------当前浏览器是：{browser}-------")
                        cls.__driver = webdriver.Firefox(service=FS(firefox_driver_path))
                    elif browser.lower() == "edge":
                        logger.info(f"-------当前浏览器是：{browser}-------")
                        cls.__driver = webdriver.Edge(service=ES(edge_driver_path))
                    elif browser.lower() == "chrome":
                        logger.info(f"-------当前浏览器是：{browser}-------")
                        cls.__driver = webdriver.Chrome(service=CS(chrome_driver_path))
                    else:
                        logger.error(f"-------暂时不支持当前浏览器：{browser}，请更换一款浏览器！(暂时支持Chrome，Firefox，edge)-------")
                        raise KeyError(f"暂时不支持当前浏览器：{browser}，请更换一款浏览器！(暂时支持Chrome，Firefox，edge)")

                return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            # 退出后，重新置空__driver
            cls.__driver = None
            
if __name__ == '__main__':
    browser = CommonConfig().get_value("browser_type", "browser")
    dd = CommonDriver().get_driver(browser)
    start_url = CommonConfig().get_value("urls", "dafault_url")
    dd.get(start_url)
    # CommonDriver().quit_driver()