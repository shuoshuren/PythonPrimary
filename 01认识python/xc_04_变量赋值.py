# 变量赋值
phone = "123456"
# 输出变量使用 print语句
print(phone)

# str是字符串类型
name = "小明"
# int 是整数类型
age = 12
# bool 表示布尔类型，true或者false
gender = True
# float 表示是小数类型，浮点数
height = 1.75

weight = 75.0

# type() 查看变量类型

# 字符串变量通过“+”可以进行拼接

print(name+phone)

# 字符串变量可以和数字通过“*”进行相同的拼接

print("="*32)

# 除此之外，字符串和数字变量不能进行任何计算

# print("123"+123)

"""
变量的输入
输入是指用代码获取用户通过键盘输入的信息，在Python中采用input()函数获取键盘的输入信息
input() 获取的数据类型都是str字符串类型
字符串变量 = input(提示信息)

类型转换函数：
int(x) 将x转换为整数
float(x) 将x转换为浮点数
"""
# 输入单价和重量
price_str = input("请输入单价：")
weight_str = input("请输入重量：")
# 将str转换为float进行计算
price = float(price_str)
weight = float(weight_str)
money = weight*price
# 将float转换为Str进行输出
print("总价："+str(money))

"""

格式化输出

如果希望输出文字信息的同时，一起输出数据，就需要使用到格式化操作符

% 被称为格式化操作符，专门用于处理字符串中的格式

包含%的字符串，被称为格式化字符串

%s 字符串

%d 有符号十进制整数

%f 浮点数

%% 输出%

语法格式：
print("格式化字符串" % 变量1)

print("格式化字符串" % (变量1,变量2...))

"""

print("单价：%f ，总量：%f ，总价：%f" % (price,weight,money))
