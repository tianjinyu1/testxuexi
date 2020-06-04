"""
# 模拟管理员登陆
from func import chaxun 
username = input("请输入账号:")
password = input("请输入密码:")
sql = 'select * from t_admin where username ="{}" and password = "{}"'.format(username,password)
print(sql)
res = chaxun(sql)
if len(res) != 0:
    print("管理员登陆成功!")
else:
    print("管理员登陆失败!")
"""

# 模拟注册
from func import chaxun 
from func import commit
username = input("请输入账号:")
password = input("请输入密码:")
sql1 = 'INSERT into t_admin values(NULL, "testadmin1", "admin123", NULL, NULL, "管理员2", "好好学习啊", "headimg.jpg", NULL, "女", 0, NULL, NULL, NULL)'
res1 = chaxun(sql1)
if res1 == True:
    sql2 = 'select * from t_admin where username ="{}" and password = "{}"'.format(username,password)
    print(sql2)
    res2 = chaxun(sql2)
    if len(res2) != 0:
        print("此账号已注册！")
    print("注册成功!")
else:
    print("注册失败")
