#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2020/7/1 0:23

import sys
sys.path.append("..")
sys.path.append(r"F:\WebUiAutomation")
import subprocess
import chardet
import winreg




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




if __name__ == '__main__':
    cmd = 'netstat -ano'
    dd = DisposeCommand.dispose_cmdline(cmd)
    print(dd)
