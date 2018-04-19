name_list = ["张三","李四","王五","马六","张三"]

# len (length 长度）函数可以统计列表中元素的总数
list_len = len(name_list)
print("list长度：%d" % list_len)

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("张三")
print("张三出现的次数：%d" % count)
# 从列表中删除数据,如果数据不存在，则会报错
name_list.remove("张三")
count = name_list.count("张三")
print("张三出现的次数：%d" % count)
print(name_list)
