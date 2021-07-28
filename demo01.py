
# print("hellow,python")  #字符串
# print(123)              #整数
# print(1.11)             #小数
# print(True)             #布尔值
# print(())               #元组
# print([])               #数组
# print({})               #字典


# 元组，下标，从0开始编号，带负号 从右侧开始编号

# a=(1,22,"哈哈",True,False,"哈哈","sda")
# print(a.index("哈哈"))
# print(a.count("哈哈"))

#切片, 左闭右开
# print(a[0:3])
# print(a[3:5])
# print(a[5:])

#二维元组
# b=(a,"sdf",12,"哈哈")
# print(b[0][1])
# print(a[-2])

#数组  数组与元组区别 元组写好过后不可以修改，数组可以修改

# a=[1,2,3,"sss","ssd"]
# a.append("append1")
# a.insert(1,"insert")
# print(a)

#字典 1、字典中的值没有顺序。2、字典的结构必须是 键值对的结果 ：key：value

# a={"name":"张三","age":18}
#  #取值
# print(a["name"])
# #新增
# a["high"]=180
# print(a)
# #修改
# a["name"]="李四"
# print(a)

a=input("请输入你的名字：")
b=input("请输入你的年龄：")
c=input("请输入你的性别：")
cun={"name":a,"age":b,"sex":c}
print("个人信息:","名字："+a,"年龄："+b,"性别："+c)