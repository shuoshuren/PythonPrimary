"""
应用场景：
1.函数的参数和返回值，一个函数可以接收任意多个参数，或者一次返回多个数据
2.格式化字符串，格式化字符串后面的()本质就是一个元组
3.让列表不可以被修改，以保护数据安全

"""

# 格式化字符串
info_tuple = ("xiaoming",20,1.85)
print("%s 年龄：%d 身高：%0.2f" %info_tuple)

"""
元组和列表相互转换
使用list函数可以将元组转换为列表
使用tuple函数可以将列表转换为元组
"""
# tuple()
num_list = [1,2,3,6,1]
print(type(num_list))
num_tuple = tuple(num_list)
print(type(num_tuple))

