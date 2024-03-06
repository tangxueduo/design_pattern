# coding=utf-8
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):

    def pay(self, money):
        return f"cost {money}"


class JDPay(Payment):
    def pay(self, money):
        return f"cost {money}"


class WechatPay(Payment):
    def cost(self, money):
        return f"cost {money}"


# ----简单工厂, 不直接向客户暴露对象创建的实现细节，
# 缺点： 违背单一职责（因为集中到一个工厂）违背开闭 （当添加新产品时，需要修改工厂类代码）
class PaymentFactory:
    def choose_payment(self, method):
        if method == "alipay":
            return AliPay()  # 隐藏了这个类的实例化
        elif method == "wechat":
            return WechatPay()
        else:
            raise TypeError("not found tool to payment.")


# -----抽象工厂 思想： 工厂子类来创建一系列相关或者相依赖的对象
# example: 生产手机(外壳 + cpu + operate system)
