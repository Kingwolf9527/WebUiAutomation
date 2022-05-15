# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2020/8/1 4:16

import sys
import time
import atexit
import pymysql
from pymysql.cursors import DictCursor
from dbutils.pooled_db import PooledDB
from common.common_config import CommonConfig
from common.common_convert_data_type import CommonConvertData
from common.common_log import CommonLog

sys.path.append("..")
sys.path.append(r"F:\WebUiAutomation")
logger = CommonLog.get_logger()

# 数据库配置数据处理
conf = CommonConfig()
mysql_info = {
    "host": conf.get_value('dbutils_mysql_conf', 'host'),
    # 端口注意为数字类型
    "port": int(conf.get_value('dbutils_mysql_conf', 'port')),
    "user": conf.get_value('dbutils_mysql_conf', 'user'),
    "password": conf.get_value('dbutils_mysql_conf', 'password'),
    "db": conf.get_value('dbutils_mysql_conf', 'db'),
    "charset": conf.get_value('dbutils_mysql_conf', 'charset'),
    # 设置的数值为整形，不是字符串
    "mincached": int(conf.get_value('dbutils_mysql_conf', 'mincached')),
    "maxcached": int(conf.get_value('dbutils_mysql_conf', 'maxcached')),
    "maxconnections": int(conf.get_value('dbutils_mysql_conf', 'maxconnections')),
    # 阻塞判断是布尔值(调用字符串转布尔值方法)
    "blocking": CommonConvertData().string_to_bool(target=conf.get_value('dbutils_mysql_conf', 'blocking'))
}


class CommonDbutils(object):

    def __init__(self):
        # # 注册一个自动退出函数,拥有与__del__函数同样的效果
        atexit.register(self.dealloc)
        self.conf = CommonConfig()
        self.host = self.conf.get_value('dbutils_mysql_conf', 'host')
        # 端口注意为数字类型
        self.port = int(self.conf.get_value('dbutils_mysql_conf', 'port'))
        self.user = self.conf.get_value('dbutils_mysql_conf', 'user')
        self.password = self.conf.get_value('dbutils_mysql_conf', 'password')
        self.db = self.conf.get_value('dbutils_mysql_conf', 'db')
        self.charset = self.conf.get_value('dbutils_mysql_conf', 'charset')
        # 设置的数值为整形，不是字符串
        self.mincached = int(self.conf.get_value('dbutils_mysql_conf', 'mincached'))
        self.maxcached = int(self.conf.get_value('dbutils_mysql_conf', 'maxcached'))
        self.maxconnections = int(self.conf.get_value('dbutils_mysql_conf', 'maxconnections'))
        # 阻塞判断是布尔值(调用字符串转布尔值方法)
        target = self.conf.get_value('dbutils_mysql_conf', 'blocking')
        self.blocking = CommonConvertData().string_to_bool(target=target)
        try:
            # 指定数据库连接驱动以及最大连接数
            self.pooldb = PooledDB(creator=pymysql, mincached=self.mincached, maxcached=self.maxcached,
                                   maxconnections=self.maxconnections, blocking=self.blocking,
                                   host=self.host, user=self.user, password=self.password,
                                   port=self.port, database=self.db, charset=self.charset)
            logger.info('------ Database Connected Successul！------')
        except IOError:
            logger.error('------ Database Connected Failed！------')
        else:
            # 建立连接以及创建游标
            self.conn = self.pooldb.connection()
            # 返回结果以字典形式表示
            self.cur = self.conn.cursor(DictCursor)

    def dealloc(self):
        """
        关闭数据库（对象资源被释放时触发，在对象即将被删除时的最后操作）
        @return:
        """
        # 关闭游标
        self.cur.close()
        logger.info('\r\n' + '------ Closed cur！------')
        # 关闭数据库连接
        self.conn.close()
        logger.info('------ Closed Database！------')

    def query_db(self, sql):
        """
        负责查询数据库数据
        @param sql:
        @return:
        """
        try:
            start_time = time.time()
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            result = self.cur.fetchall()
            logger.info(f'------ result is : {result} ------')
            end_time = time.time()
            logger.info(f'消耗的时间为：{end_time - start_time}s')
            return result
        except ValueError:
            logger.error('\r\n' + '------ Error: unable to fecth data ------')
            logger.error(f'------ SQL data is : {sql} ------')

    def execute_db(self, sql):
        """
        负责更新/插入/删除数据库数据
        @param sql:
        @return:
        """
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 执行SQL语句
            self.cur.execute(sql)
            # 需要提交数据，才生效
            self.conn.commit()
            logger.info(f'------ SQL data is : {sql} ------')
        except Exception as e:
            logger.error('\r\n' + f'------ 操作MySQL出现错误，错误原因：{e} ------')
            logger.error(f'------ SQL data is : {sql} ------')
            # 需要回滚处理
            self.conn.rollback()


if __name__ == '__main__':
    sql = "select * from mainboard " \
          "where mainboard.mainboard_type like '%玩家国度%' " \
          "order by mainboard.price DESC;"
    d = CommonDbutils()
    result = d.query_db(sql)
    print(result)
