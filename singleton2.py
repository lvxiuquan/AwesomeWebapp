# -*-coding=utf-8-*-

'''
单例模式-使用共享属性
'''


class SssTon(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(SssTon, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass(SssTon):
    aa = 1


a = MyClass()
b = MyClass()
print id(a), id(b)
print a.aa, b.aa
a.aa = 44
print a.aa, b.aa
print id(a.__dict__), id(b.__dict__)
