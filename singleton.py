# coding=utf-8


# 单例模式,   一种锁
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 调用父类new创建实例
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Myclass(Singleton):
    def __init__(self, a):
        self.a = a


a = Myclass(10)
b = Myclass(13)

print(a.a, b.a)
a is b  # True
