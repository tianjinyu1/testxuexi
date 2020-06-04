# 类
"""
class person():
    #变量：成员变量：类中的变量
    mz = "索隆"
    xb = "男"
    age = 18
    zs = "三千世界"
    # 功能：成员方法：类中的方法
    def talk(self): #self是成员方法的的第一个参数，是Python的语法要求
        print("{}海贼王".format(self.mz))
    def eat(self, dx):
        print("路飞，最爱吃{}".format(dx))
        return"吃肉了"
    
    def test(self):
        self.talk()
        a = self.eat("利库")
        print(a)
# 实例化类：person（）
#p:实例化对象
p = person()
# print(p.mz)
# print(p.xb)
# print(p.age)
# print(p.zs)
# p.talk() #调用方法
a = p.eat("肉") #dx= 肉。self本身是不用管的
print(a)

"""s


class Person1():
    xm = "旋涡鸣人"
    #构造方法：_init_,在实例化类的时候给新建、初始化成员变量；固定写法
    def __init__(self,nl):
        self.age = nl #新建一个成员变量age
# self:如果成员变量没有写，则新建一个，写了就直接可以赋值  
p = Person1(28)
print(p.xm)
print(p.age)
