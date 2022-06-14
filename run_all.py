# -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/5/28 18:50
#   @File      :    run_all.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append("..")
sys.path.append(r"F:\WebUiAutomation")
import os
import pytest
from common.common_log import CommonLog
from common.common_file_path import allure_json_path, allure_html_path
from common.common_dispose_cmd import DisposeCommand

logger = CommonLog.get_logger()


class TestRunAll(object):

    def run_all(self):

        # allure报告的路径
        logger.info(f"----------json_path的目录为：{allure_json_path}----------")
        logger.info(f"----------allure_path的目录为：{allure_html_path}----------")

        if not os.path.exists(allure_json_path):
            os.makedirs(allure_json_path)
        if not os.path.exists(allure_html_path):
            os.makedirs(allure_html_path)

        # 执行pytest用例，生成数据
        args = [f'--alluredir={allure_json_path}']
        pytest.main(args)

        # 根据生产的数据，生成测试报告
        cmd = f'allure generate {allure_json_path} -o {allure_html_path} --clean'
        try:
            DisposeCommand.dispose_cmdline(cmd)
        except Exception as e:
            logger.error('----------执行测试用例失败，请检查环境配置！----------')
        # 发送邮件(交给Jenkins处理)

if __name__ == '__main__':
    TestRunAll().run_all()