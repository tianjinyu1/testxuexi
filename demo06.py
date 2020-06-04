# # 自带的包
# import time # 时间相关 time。sleep（3）
# import sys # 系统相关
# import unittest #
# 第三方的包 要使用pip、pip3工具;
# pip -V 查看pip的版本；
# pip list 列出已经安装的第三方的包
# pip install 包的名字 安装   但是有cmd权限
# 测试常用的第三方包 -i 参数是加快下载
# selenium 是用于web自动化测试 pip install selenium  -i https://pypi.tuna.tsinghua.edu.cn/simple 下载的来源是清华源
# requests 接口自动化测试 pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
# pymasql python读写mysql数据库 pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
# 导入是import from是包名 import类/变量/参数；导入的方式由包来决定
# 自定义的包：把文件变成报，可以在不同的文件夹下面导入代码；在文件夹下添加一个_init_py空白文
# Python的异常处理
# 什么异常：代码报错，没有办法继续执行
# 如果代码报错还想继续运行后面的代码，必须使用异常处理


"""
def chengfa(a,b): #def就是定义一个方法！固定的！
    """
    这个方法是实现一个输入两个数字，输出他们乘积 
    """
    ji = a * b
    return ji  #return是返回值
c = 2
f = 4
d = 9
s1 = chengfa(c,d)
s2 = chengfa(f,d)
print(s1)
print(s2)
"""