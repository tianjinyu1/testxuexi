#包（1、系统自带D:\Python\Lib；
#   2、第三方的包:pip就是来管理第三方包的工具。
#   pip list:查看已经安装的第三方的包；pip install 包名：安装第三方的包；pip uninstall 包名：卸载安装的包）
#常见的第三方的包：1、pymysql 操作mysql数据库的
# --》模块--》类--》方法--》变量；既包含又平等
#print("哈哈") #方法名：print；参数：哈哈
#实现一个输入任意的两个数字，输出他们的和的方法
def chengfa(a,b): #def就是定义一个方法！固定的！
    """
    这个方法是实现一个输入两个数字，输出他们乘积
    """
    print(a*b)
chengfa(12,10) #可以导入别的文件里面使用，路劲：import func/func.chengda;2、from func impor chengfa
import pymysql
def chaxun(sql):
    """
    数据库查询
    """
    db = pymysql.connect(host="192.144.148.91",user="ljtest",password="123456",db="ljtestdb") #这个是链接数据库,且需要游标
    #游标，有游标才能进行输入
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close
    print(res)


chaxun("show tables;") #定义的查询的方法就好了，可以导入到别的文件中
    