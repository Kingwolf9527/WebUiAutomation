# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/6/4 22:41
#   @File      :    conftest.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append("..")
sys.path.append(r"/")
import pytest
from common.common_log import CommonLog
from common.common_driver import CommonDriver

logger = CommonLog.get_logger()

# _driver = None
# # 处理多线程会出现的单例模式问题
# _driver_lock = threading.Lock()
#
# def common_driver():
#     """
#     浏览器类型：谷歌，edge，火狐或者其他
#     @return:
#     """
#     global _driver
#     global _driver_lock
#     browser = CommonYaml(base_config_path).read_yaml()['browser_type']
#     # 外层校验是为了避免单例已产生后，线程还要拿锁，浪费锁资源
#     if _driver is None:
#         with _driver_lock:
#             # 内层校验是单例逻辑的条件判断，必须放在锁内，是为了避免线程在等锁的过程中单例已产生
#             if _driver is None:
#                 # __driver = getattr(webdriver, browser)(executable_path=chrome_driver_path)
#                 if browser.lower() == "firefox":
#                     logger.info(f"-------当前浏览器是：{browser}-------")
#                     _driver = webdriver.Firefox()
#                 elif browser.lower() == "edge":
#                     logger.info(f"-------当前浏览器是：{browser}-------")
#                     _driver = webdriver.Edge()
#                 elif browser.lower() == "chrome":
#                     logger.info(f"-------当前浏览器是：{browser}-------")
#                     _driver = webdriver.Chrome()
#                 else:
#                     logger.error(f"-------暂时不支持当前浏览器：{browser}，请更换一款浏览器！(暂时支持Chrome，Firefox，edge)-------")
#                     raise KeyError(f"暂时不支持当前浏览器：{browser}，请更换一款浏览器！(暂时支持Chrome，Firefox，edge)")
#
#             return _driver


@pytest.fixture(scope="session")
def get_driver():
    driver = CommonDriver().get_driver()
    yield driver
    # CommonDriver().quit_driver()
    
    