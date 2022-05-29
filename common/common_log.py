# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/7/13 22:47

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import os
import threading
import logging
from logging import handlers



class CommonLog(object):
    logger = None
    _logger_lock = threading.Lock()

    @classmethod
    def get_logger(cls):
        with cls._logger_lock:
            if cls.logger is None:
                # 获取logger对象
                cls.logger = logging.getLogger()
                cls.logger.setLevel(logging.INFO)

                # 设置log的保存文件
                log_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) \
                           + '/logs/' + 'file_log.log'
                log_file_error = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) \
                                 + '/logs/' + 'file_log_error.log'

                if not cls.logger.handlers:
                    # 创建handler(包括文件以及控制台)
                    cls.file_handler = handlers.TimedRotatingFileHandler(filename=log_file, when='midnight',
                                                                         interval=1, backupCount=30, encoding="utf-8")
                    cls.file_handler.setLevel(logging.INFO)

                    cls.file_error_handler = handlers.TimedRotatingFileHandler(filename=log_file_error,
                                                                               when='midnight', interval=1,
                                                                               backupCount=30, encoding="utf-8")
                    cls.file_error_handler.setLevel(logging.ERROR)

                    cls.stream_handler = logging.StreamHandler(sys.stdout)
                    cls.stream_handler.setLevel(logging.INFO)

                    # 设置输出格式
                    format_time = "%(asctime)s---[%(levelname)s]---[%(name)s]---" \
                                  "[%(filename)s---%(funcName)s---%(lineno)d]---%(message)s"
                    log_format = logging.Formatter(format_time)

                    # handler格式化处理
                    cls.file_handler.setFormatter(log_format)
                    cls.file_error_handler.setFormatter(log_format)
                    cls.stream_handler.setFormatter(log_format)

                    # logger对象添加handler
                    cls.logger.addHandler(cls.file_handler)
                    cls.logger.addHandler(cls.file_error_handler)
                    cls.logger.addHandler(cls.stream_handler)

            return cls.logger


if __name__ == '__main__':
    dd1 = CommonLog.get_logger()
    dd1.info("---------king555555来测试一下数据6！！1-------------------")
    dd1.error("--------可能的错误log需要test验证5！！！---------------------------")
