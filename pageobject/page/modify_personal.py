#   -*- coding: utf-8 -*-
#   @Author    :    KingWolf
#   @Time      :    2022/10/19 3:33
#   @File      :    modify_personal.py
#   @Project   :    WebUiAutomation

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import time
import re
from ..base.base_handle import BaseHandle
from common.common_file_path import icon_path, autoit_file
from common.common_dispose_cmd import DisposeCommand

class ModifyPersonal(BaseHandle):
    
    def modify_info(self, **kwargs):
        """
        修改个人信息
        @param kwargs:
        @return:
        """
        # 悬停进入“个人信息”页面
        self.mouse().move_to_element(self.find_element_highlight(kwargs["personal"]["account_setting"])).perform()
        self.click(kwargs["personal"]["personal_info"])
        time.sleep(1)
        # 修改头像
        self.click(kwargs["personal"]["icon"])
        time.sleep(2)
        # 切换iframe
        self.iframe_into(kwargs["personal"]["upload_iframe"])
        time.sleep(2)
        # 第一种方式:pathlib获取的路径为类，需要转为str类型
        self.upload_file(kwargs["personal"]["upload_button"], str(icon_path))
        # # 第二种方式:使用第三方工具的autoIT
        # self.upload_file_click(kwargs["personal"]["upload_button"])
        # time.sleep(2)
        # # Python执行生成的exe文件
        # DisposeCommand.execute_file(str(autoit_file))
        # time.sleep(1.5)
        # 获取上传图片大小([共1份（39.13K），已上传1份])
        self.get_img_size = self.get_element_text(kwargs["personal"]["img_size"])
        self.images_size = re.findall("份（(.*)）", self.get_img_size)[0]
        self.click(kwargs["personal"]["img_save_button"])
        # 退出iframe
        self.iframe_out()
        # 修改昵称
        self.input(kwargs["personal"]["nickname"], kwargs["personal"]["new_nickname"])
        time.sleep(0.5)
        # 修改性别
        self.click(kwargs["personal"]["sex"])
        time.sleep(0.5)
        # 修改生日(也可以通过js修改)
        self.input(kwargs["personal"]["birthday"], kwargs["personal"]["new_birthday"])
        # self.execute_js(kwargs["personal"]["new_birthday_js"])
        time.sleep(0.5)
        # 最后确认保存按钮
        self.click(kwargs["personal"]["save_button"])
        time.sleep(2)
        # 判断修改成功标志
        self.success_flag = self.get_element_text(self.find_element_highlight(kwargs["personal"]["success_modify"]))
        self.forecast_text = kwargs["personal"]["flag_text"]
