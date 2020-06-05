# requests 接口测试 1、构造请求；2、判断结果；3、数据库数据对比
import requests
from func import chaxun

 # get接口请求
# url = "http://192.144.148.91:2333/get_title_img?num=3" # 接口信息，类似于postman的URL
# res = requests.get(url)  # 发送请求并且获取返回值，返回值给res 
# print(res.text) # 打印返回值的信息
 

# post登陆接口请求
# u = "http://192.144.148.91:2333/login"  
# d = {"username":"tunan","password":"asd123456"} 
# res = requests.post(url=u,json=d) #使用post方法向接口u接口请求，并且使用json格式的数据传参数
# print(res.text)

#token要从登陆之后来取
# token = res.json()["data"]["token"] # res.json()把返回值变成Python的字典


# # 评论文章
# u1 = "http://192.144.148.91:2333/comment/new"
# d1 = {"ctype": 1, "comment": "奥克兰技术的flak即使对方", "fid": "3796"} 
# h1 = {"token":"token"}
# res = requests.post(url=u1,json=d1,headers=h1)  # headers:请求头
# print(res.text)

# request请求 支持参数来指定get或者post ，同get和post用法看自己习惯用哪个
u = "http://192.144.148.91:2333/get_title_img?num=3"
res = requests.request("get",url=u)

u = "http://192.144.148.91:2333/login"  
d = {"username":"tunan","password":"asd123456"} 
res = requests.request("post",url=u,json=d) #使用post方法向接口u接口请求，并且使用json格式的数据传参数
print(res.text)


# 判断结果：http状态码/结果码
# 断言：如果条件成立，断言通过，否则直接断言异常；自动化测试中，使用断言进行判断结果
assert res.status_code == 200 # res.status_code 调用接口里的状态码,断言状态码
assert res.json()["status"] == 200 #完成结果码判断

# 查询数据库
# sql = "select * from t_user where username = '{}'".format(d.get("username"))
# if len(chaxun(sql)) != 0:
#     print("结果测试通过！")
# else:
#     print("接口测试失败！")
