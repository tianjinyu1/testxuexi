#判断:判断的符号：>、<、==、in（）、is、！=、between
# a = 3 把3这个值赋值给a这个变量
"""
age = float(input("请输入年龄："))
if age >= 18:
    print("成年人")
else:
    print("未成年") #这句和上面的else即顶格行和缩进行是属于一个代码块 ，判断语句是固定
"""

# a = "下路班艾希" #这个就是来判断in的，意思就是能否在一个变量中是否在另一个变量中；not in判断元素不存在，是同样的用法
# b = "下路班"
# if b in a:
#     print("艾希是ad")
# else:
#     print("不是")

# a = "ad"
# b = "uzi"
# if a is b:  #is是来判断两个变量地址是否相同 ==是来判断内容是否相同
#     print("a是b的本身")
# else:
#     print("a不是b的本身")


# #for循换,遍历,就是按着名字读一遍 ,元祖、数组、字符串遍历的方法一样
# cc = [1,2,3,"哈哈哈","和嘿嘿",True,"回锅肉",3,"小龙虾",3,4,1,False] 
# for i in cc:
#     print(i)

#while循换
a = 0
while a < 20:
    print("哈哈哈",a)
    a = a + 1 # 类似自动递增的