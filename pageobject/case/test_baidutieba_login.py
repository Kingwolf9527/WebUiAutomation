# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2022/4/14 23:34

import pytest
from ..page.login_page import LoginPage

class TestTiebaLogin(object):

    def test_login(self):
        d = LoginPage(browser="chrome")
        d.go_sign("1069645896@qq.com", "922521dfxs5619")


if __name__ == '__main__':
    pytest.main()