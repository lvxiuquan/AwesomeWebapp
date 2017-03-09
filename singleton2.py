# -*-coding=utf-8-*-

'''
单例模式-使用共享属性
'''


class YouAreBoy(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(YouAreBoy, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class YourClass(YouAreBoy):
    aa = 1
    bb = 2


a = YourClass()
b = YourClass()
print id(a), id(b)
print a.aa, b.aa
a.aa = 44
print a.aa, b.aa
print id(a.__dict__), id(b.__dict__)
