# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/7/16 6:03

import sys
import os
import configparser
from common.common_log import CommonLog
from common.common_file_path import config_path

sys.path.append("..")
sys.path.append(r"F:\WebUiAutomation")
logger = CommonLog.get_logger()

class CommonConfig(object):

    def __init__(self, file_path=config_path):
        # 读取配置文件
        self.cf = configparser.ConfigParser()
        if not os.path.exists(file_path):
            logger.error("------- 请确保配置文件存在! -------")
        self.cf.read(filenames=file_path, encoding="utf-8")

    def get_value(self, selection, key):
        try:
            result = self.cf.get(selection, key)
            logger.info(f"------- 获取到指定配置文件的值，selection：{selection}---key：{key}---result：{result} -------")
        except ValueError:
            logger.error(f"------- 没有获取到指定配置文件的值，selection：{selection}---key：{key} -------")
            result = None
        return result

if __name__ == '__main__':
    dd = CommonConfig()
    rr = dd.get_value("urls", "dafault_url")

