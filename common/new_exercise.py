# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2022/3/5 4:01


class A:

    def __init__(self, param=[]):
        self.param = param

    def pick(self, name):
        self.param.append(name)




a = A()
b = A()
c = A()

a.param = [1]
b.pick([2])

# 请问a，b，c的param各是多少？
print(a.param)
print(b.param)
print(c.param)

