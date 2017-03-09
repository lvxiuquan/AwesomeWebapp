# -*-coding=utf-8-*-

'''
单例模式-使用__new__方法
'''


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    aa = 1


a = MyClass()
b = MyClass()
print id(a), id(b)
print a, b
