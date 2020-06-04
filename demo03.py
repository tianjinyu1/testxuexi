#判断:判断的符号：>、<、==、in（）、is、！=、between

a = 3 #把3这个值赋值给a这个变量
if a > 1:
    print("a大于1")
else:
    print("a小于等于1") #这句和上面的else即顶格行和缩进行是属于一个代码块 ，判断语句是固定

"""
age = int(input("请输入你的年龄："))
if age > 65:
    print("退休享受夕阳红")
elif age > 30: 
    print("成年人保温杯里泡枸杞！") 
elif age > 20:
    print("青春正好，不负韶华")
elif age > 18 and age < 24:
     print("年轻就要燥起来！")
elif age > 12:
    print("好好学习，天天向上！")   
else:      #ps:判断循环中只有最后一句是else，中间的是elif
    print("我还是个宝宝呀！")  
"""
    
""" 
name = input("请属于你的名字：")
if name == "小仙女"：
     print("小仙女真漂亮！")
else:
    print("你好陌生人！")

bb = ["小仙女","小精灵","小女巫","小药师"]
if name in bb:
    print("都是召唤师！")
else:
    print("背叛者！")
if type(name) is str:
    print("输入的都是字符串！")
"""

"""
#小练习：通过input获取账号和密码， 如果输入的值满足账号大于5位并且小于12位，密码是8-16位，
# 那么把账号密码存到一个字典中；如果不满足条件，请提示原因!
a = input("请输入你的账号：")
b = input("请输入你的密码：")
c = len(a)
d = len(b)
ww = {"user":a,"password":b}
if c >= 5 and c <= 12: #大于5小于12
    if d >= 8 and  d <= 16: #判断里面加判断，即是嵌套！
       print(ww)
    else: #注意代码的缩进
      print("密码不规范！")
else:
      print("账号不规范！")
"""

"""
#while循换
a = 0
while a < 20:
    print("哈哈哈",a)
    a = a + 1
"""


"""
#小练习：请使用while循环，自动的把一个数组中的下标为单数的值，依次打印出来
cc = [1,2,3,"哈哈哈","和嘿嘿",True,"回锅肉",3,"小龙虾",3,4,1,False] 
a = 1
while a < len(cc):
    print(cc[a]) #取值
    a = a + 2 #1+2为3为单数，进行循环！
"""


"""
#for循换,遍历,就是按着名字读一遍
cc = [1,2,3,"哈哈哈","和嘿嘿",True,"回锅肉",3,"小龙虾",3,4,1,False] 
for i in cc:
    print(i)
"""


"""
#小练习：请使用for循环，自动的把一个数组中的下标为单数的值，依次打印出来
cc = [1,2,3,"哈哈哈","和嘿嘿",True,"回锅肉",3,"小龙虾",3,4,1,False] 
i = 1
for i in range(1,len(cc),2):
    print(cc[i])
"""


"""
for i in range(99): #0-98
    print(i)
#range(10) 0-9
#range(8,10) 8-89
#range(0,10,2) 0 2 4 6 8 #
#print(list(range(0,10,3)) #步进  i
"""


"""
#小练习：请使用for循环，打印99乘法表出来
for a in range(1,10):
    for b in range(1,a+1):
        print(a,"X",b,"=",a*b,end="  ")
    print()
"""


"""
#小练习：现在有10个学生的成绩，需要录入到系统中.
#这是个人分别是，张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、朱珠、亚索
#并且名字和成绩需要对应上。而且大于60的和小于60的需要分开存放。
a = 0 #定义一个a这个变量来控制下标的变量
highscore = {} #定义一个空的字典来存放分数大于60的信息
lowscore = {} #定义一个空的字典来存放分数小于60的信息 
#(studetlist=["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
#for i in studentlist:
#score=int(input("请输入"+i+"的成绩:"))
#   if score >= 60:
#       highscore[i] = score 
#    else:
#       lowscore[i] = score
#print(highscore,lowscore))另一种写法
while a < 10: 
    name = input("请输入姓名：") 
    score = int(input("请输入成绩："))
    if score >= 60:
        highscore[name] = score   
    else:
        lowscore[name] = score
    a = a + 1
highscore.sort()
lowscore.sort()
print(highscore)
print(lowscore)
"""


"""
#小练习：通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
light={"红灯":31,"绿灯":36,"黄灯":6}
for i in light:
    for b in range(1,light[i]):
        print(i,"还有:",light[i]-b,"秒")
"""

"""
#break是中止的意思
studentlist=["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
a = 0
#while a < len(studentlist):
#  if studentlist[a] == "二狗":
#       break #中止
#  print(studentlist[a])
#   a=a+1
"""

"""
for i in studentlist:
    if i == "二狗":
        continue #跳过
    print(i)
"""

"""
while a < len(studentlist)-1: 
    a=a+1
    if studentlist[a] == "二狗":
       continue 
    print(studentlist[a]) #continue的不用写法
"""

ss

"""
import func
func.chengfa(12,10)

from func import chengfa
chengfa(12,10)#导入定义的方法
"""


