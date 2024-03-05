# coding=utf-8
from abc import abstractmethod, ABCMeta

"""
    使本来不兼容的接口，可以一起工作，类比电源适配器
"""
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

# 方法一 ：类适配器，使用继承
# class NewWechatPay(WechatPay, Payment): # 继承多个类时，高的祖先在后面
#     def pay(self, money):
#         return self.cost(money)
    
# obj = NewWechatPay()
# print(NewWechatPay.__mro__) # 查看继承顺序
# print(obj.pay(100))

# 方法二： 对象适配器，使用组合
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money): 
        return self.payment.cost(money)




