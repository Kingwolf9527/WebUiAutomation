#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2020/7/1 0:23

import sys
import subprocess
import chardet
import winreg

sys.path.append("..")
sys.path.append(r"F:\WebUiAutomation")



class DisposeCommand(object):

    @classmethod
    def dispose_cmdline(cls, cmd):
        # stdin是标准输入，返回值是标准输出和标准出错
        std_pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
        # 返回结果是字节类型
        stdout, stderr = std_pipe.communicate()
        # 获取编码方式
        get_encoding = chardet.detect(stdout)["encoding"]
        output = stdout.decode(get_encoding)
        return output

    @classmethod
    def get_browser_version(cls, browser):
        """
        获取指定浏览器的主版本
        @param browser:
        @return:
        """
        if browser.lower() == "chrome":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Google\Chrome\BLBeacon")
            version = winreg.QueryValueEx(key, "version")[0]
            return version.split(".")[0]

        if browser.lower() == "edge":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Edge\BLBeacon")
            version =  winreg.QueryValueEx(key, "version")[0]
            return version.split(".")[0]


if __name__ == '__main__':
    cmd = 'netstat -ano'
    dd = DisposeCommand.dispose_cmdline(cmd)
    print(dd)

    # dd = DisposeCommand.get_browser_version(browser="chrome")
    # print(dd)