#基础的数据结构
"""
name = input("请输入ad: ")
print("输入的ad的姓名是：",name)
#变量和赋值(整个编程里面最核心的重点内容)
# a = 1  将1这个值赋值给a这个变量，即a是变量，整个过程是赋值
"""

"""
# 小练习1：通过input分别获取两个值，然后打印出他们相加的结果,这个例子是因为是字符串，相加的结果是拼接的
a = input("请输入一个值：")
b = input("请输入另一个值: ")
print("两个相加为：",a+b)
"""

# type是获取数据的类型，下面是例子;
# print("哈哈哈的类型；",type("哈哈哈"))
# ps:str代表的是字符串；整数是int；小数是float；布尔值是bool(True/False)；空是None/Type;元组是tuple
# 数组是list/列表； 字典是dict;


"""
# 小练习2：通过input分别获取2个值，然后打印出他们相加为数值的结果,
a = input("请输入一个值：")
b = input("请输入另一个值: ")
print("两个相加为：",float(a)+float(b)) #ps:这里int或者float是用来转化成整数或者小数，且float包含了int
# 转化的方式有很多，可以在input前面加int；
#python的数据转换的规律：
# 1、任何数据都可以转换成字符串；
# 2、字符串转换成数字需要满足‘长得像’这个规律（ps:长得像即是阿拉伯数字）；
# 3、字符串可以转换成元组、数组；
# 4、整数和小数都可以互相转换；
"""

"""
#len是用来获取字符串的长度
a = len("其实我是比废物东瓯hi王的狗还狗") #这里字符串里有16个字符
print(a)
"""

"""
# 小练习3：通过input分别获取2段字符串，然后获取他们的长度，并相加输出结果,
a = input("请输入一段话：")
b = input("请输入另外一段话: ")
print("这两段话的长度为:",len(a)+len(b))
"""

#print(1>1) #1>1在数学理论上是错误的，输出的结果即为False

"""
#元组即为（）,括号里面可以放数据，括号相当于一个容器，元组里面什么可以装
#下标相当于一个编号，计算机数学是从0开始数学
xx = (1,2,3,"哈哈哈","和嘿嘿",True,"111",3,"哈哈哈",3,4,1,False)
print(xx)
print(xx[3]) #这句的含义是：取元组xx里面下标为3的数据。当然这种方法用于元组里面数据少的情况
#下标取值都用中括号固定格式；因为是从0开始数数，要取‘哈哈哈’这个数据，即是3
print(xx.count(1)) #这句代表元组xx里面有多少个1，语法‘统计’是固定格式.因为True=1;False=0，所以结果为3个1
print(xx.index("哈哈哈")) #这句代表通过index来计算这个值的下标是多少；ps:计算机是从左往右算，所以只告诉第一个'哈哈哈'的下标
"""


"""
#元组里面装元组，这种叫二维元组，
xx = (1,2,3,"哈哈哈","和嘿嘿",True,"111",3,"哈哈哈",3,4,1,False)
yy = ( 1,2,3,xx)
print(yy[3]) #这句代表打印yy里面下标为3的值
print(yy[3][4]) #这句代表打印yy里面下标为3的值里面下标为4的值
print(len(yy)) #代表打印出yy里面有多少个值
print(a[0:2]) #截取：代表打印下标为0-2的值；也可以使用index、count的方法
"""

"""
#数组 list/列表
a = ["言希","温衡"]
cc = [a,1,2,3,"温思尔","温思莞",True,"辛达夷",3,"陆流",3,4,1,False] 
print(cc[0][1]) # 二维元祖取值
print(cc.index(3)) #index的用法是计算下标为3的数据
print(cc.count(3)) # count是计算有多少个是3的数据
print(cc[0:2]) #截取：代表打印下标为0-2的值
#ps:元组与数组的区别：元组不可修改，数组可以修改；例如下面可以在数组里面加一个append，在元组不可以这样加
cc.append("append") #append的意思在数组中，在末尾追加数据。代表在元组cc里面追加一个append的值
cc.insert(5,"insert") #insert的意思是插入，在下标为5的的前面插入一个insert
cc.remove("陆流") #remove是删除，删除数组中第一个陆流的值
a = cc.pop(8) #pop是取出，把下标为8的值取出来,又赋值给a这样的变量
print(a)
cc.append(a) #追加在末尾
print(cc)
cc[0] = 9 #把下标为0的值修改成9
cc.reverse() #把数组颠倒 ;sort排序只能对数字使用，数字倒序sort（reverse=true）
cc.extend([1,3,2,4]) #把数组合并并追加到末尾
#cc.clear() #把数组清空
print(cc)
#print(cc.count(1))
#print(cc.index("小龙虾"))
ww = [2,5,7,9,0,1,3]
ww.sort() #把数组的值进行排序
ww = ["a","p","r","f"]
ww.sort(reverse=True) #把数组的字符串进行倒着排序
print(ww)
"""

"""
小练习4：通过input分别输入多段字符串，然后获取他们的长度，并把长度的值分别放到数组中，并从小打大排序；
a = input()
b = input()
c = input()
d = input()
ww = [len(a),len(b),len(c),len(d)]
ww.sort()
print(ww)
"""

"""
#字典{} 键值对 key：volue；ps:字典没有下标，即字典里的值没有顺序
a = {
    "name":"永恩",
    "age":"18",
    "sex":"男"
    } #"name":"永恩"，这个就是一个值
print(a)

#a.pop()
#a.clear()
#a.get()  #对字典取值要选取key就可以了,如果key不存在，那么直接报错，如果键值对不存在，get取空值
a.update(name="亚索") #update是修改，在update里面key相当于一个变量，不需要打引号,当key不存在是即是新增
#但是不建议这种修改方式，因为字典没有下标；
a["姓名"] = "孤儿" #这种修改方式经常用
print(a.get("name")) #如果key不存在，那么返回空
print(a.pop("name")) 
print(list(a.values())) #这个是取字典里面volue的值,list是用来转换格式的
print(list(a.keys())) #这个是取字典里面key的值，以上是字典经常用的几种方式
#通用的删除方法，del,可以用来删除数组和字典,数组里面写下标，字典写key
#del a["name"]
print(a["姓名"])
"""