# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/9/12 16:56

import pytest


class TestDemo(object):

    version = 92

    @pytest.mark.run(order=2)
    def test_01(self):
        print("测试01")

    @pytest.mark.run(order=1)
    def test_02(self):
        print("测试02")

    @pytest.mark.run(order=-7)
    def test_03(self):
        print("测试03")

    @pytest.mark.run(order=-9)
    def test_04(self):
        print("测试04")

    @pytest.mark.run(order=-3)
    @pytest.mark.skipif(version >=92, reason="当前版本不执行")
    def test_skip(self):
        c = 111
        d = 0
        e = c / d
        assert e > 0

    @pytest.mark.run(order=-2)
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)
    def test_reruns(self):
        a = 1
        b = 10
        assert a > b



if __name__ == '__main__':
    pytest.main()