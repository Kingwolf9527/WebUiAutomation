#- * - coding:utf-8
#__author__ : kingwolf
#createtime : 2020/8/3 1:50

import sys
sys.path.append("..")
sys.path.append(r"F:\WebUiAutomation")

class CommonConvertData(object):

        @staticmethod
        def string_to_bool(target):
            """
            把字符串转化为布尔值
            @param target:
            @return:
            """
            if target.lower() == 'true':
                return True
            else:
                return False

        @staticmethod
        def fload_int_to_string(target):
            """
            把浮点数或者整形转化为字符串(处理excel文件的单元格的数值)
            @param target:
            @return:
            """
            if isinstance(target, (float, int)):
                target = str(int(target))
            return target



if __name__ == '__main__':
    result = CommonConvertData.string_to_bool(target='True')
    # result = CommonConvertData.fload_to_string(target=106538.0)
    # result = CommonConvertData.fload_int_to_string(target=730737319)
    print(result, type(result))

