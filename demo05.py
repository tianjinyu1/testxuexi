#去判断用户是否登录成功
# db = [{"username":"小仙女","passsword":"123456"},{"username":"小女巫","passsword":"1234567"}]
# zh = input("请输入账号：")
# mm = input("请输入密码：")
# for i in db: 
#     if zh == i.get("username"): #账号匹配
#         if mm == i.get("passsword"):
#             print("{}登录成功！".format(zh)) 
#             break #终止循环 即表示登录成功，不需要循环了
#     else: #账号并不匹配
#         #continue #跳过本次循环，开启下次循环
#         print("登录失败！")


# for i in db: # i是一个变量 bug版本
#     if zh == i.get("username") and mm == i.get("passsword"):
#         print("输入的账号{}登录成功！".format(zh)) #format是字符串拼接
#     else:
#         print("登录失败！")



# # 作业:输入账号和密码,去判断db中是否存在该账号，如果已存在，就修改账号和密码，如果不存在就新增一个字典
# db = [{"username":"chenke","passsword":"123456"},{"username":"小女巫","passsword":"1234567"}]
# 输入一个在账号为chenke，那就需要把password改成输入的密码
# 输入的账号zqc,那就新增一个字典
db = [{"username":"小仙女","password":"123456"},{"username":"小女巫","password":"1234567"}] #定义个列表
zh = input("请输入账号：")
mm = input("请输入密码：")
count = 1 #解决重复添加账号的bug
for i in db:  # i是一个key值 i就是db里的每一个元素（字典）
    if zh == i.get("username"):
        i["password"] = mm # 修改密码
        break # 退出循环
    else:
        if len(db) == count: # 限制添加次数
            a = {}
            a["username"] = zh
            a["passwor"] = mm 
            db.append(a)   # 增加字典元素  db.append({"uesrname":zh,"passwor":mm})另外一种写法
    count = count + 1
print(db) 
    