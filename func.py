#包（1、系统自带D:\Python\Lib；
#   2、第三方的包:pip就是来管理第三方包的工具。
#   pip list:查看已经安装的第三方的包；pip install 包名：安装第三方的包；pip uninstall 包名：卸载安装的包）
#常见的第三方的包：1、pymysql 操作mysql数据库的
# --》模块--》类--》方法--》变量；既包含又平等
#print("哈哈") #方法名：print；参数：哈哈
#实现一个输入任意的两个数字，输出他们的和的方法
# def chengfa(a,b): #def就是定义一个方法！固定的！
#     """
#     这个方法是实现一个输入两个数字，输出他们乘积 
#     """
#     ji = a * b
#     return ji  #return是返回值
# # chengfa(12,10) #可以导入别的文件里面使用，路劲：import func/func.chengda;2、from func impor chengfa
#参数的数据类型可以选择，且可以是任何类型



import pymysql

def chaxun(sql):
    """
        查询数据mysql数据库:只能select，不要delete update insert
    """
    # pymysql 连接数据库
    # host="192.144.148.91":数据库的ip地址 user="ljtest"：数据库登录账号, password="123456"：密码, db="ljtestdb"：数据库名字
    db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    # 获取游标 ：查询窗口
    cur = db.cursor()     
    # 执行sql语句
    cur.execute(sql) 
    # 得到执行的结果
    res = cur.fetchall()
    db.close()

    return res

# sql = "select * from t_user where id = 23123123123"
# a = chaxun(sql)
# print(a)



def commit(sql):
    """
        增加/删除/修改方法：delete update insert：不要传select
    """
    # 打开数据库
    db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    # 获取游标 ： 查询窗口
    cur = db.cursor()     
    # 执行sql语句
    cur.execute(sql) 
    # 提交修改 
    db.commit()
    db.close()
    return True

# update
# sql = "update t_user set username='mcc1234' where id=254"

# insert
# sql = 'INSERT into t_admin values(NULL, "testadmin1", "admin123", NULL, NULL, "管理员2", "好好学习啊", "headimg.jpg", NULL, "女", 0, NULL, NULL, NULL)'

# delete
sql = "delete from t_admin where id=557"
commit(sql)

