"""
列表的定义：
list(列表)是Python中使用最频繁的数据类型，在其他语言中通常叫做数组
list专门用于存储一串信息
列表用【】定义，数据之间使用，分割
类别的索引从0开始，从列表中取值时，如果超出索引范围，程序会报错
"""
name_list = ["张三","李四","王五","马六"]

# 1.取值和取索引
# IndexError: list index out of range 列表索引超出范围
print(name_list[0])

# 知道数据内容，想知道索引位置
# ValueError: '张三123' is not in list 如果传递的数据不在列表中，程序会报错
print(name_list.index("张三"))

# 2.修改
# IndexError: list assignment index out of range 列表指定的索引超出范围
name_list[1] = "lisi"
print(name_list[1])

# 3、向指定位置添加数据
# append 向列表的尾部添加数据
name_list.append("王小二")
# insert 向指定位置添加数据
name_list.insert(1,"小美眉")
# extend 把另外的列表中的完整内容，追加到当前列表的尾部
temp_list = ["孙悟空","猪八戒","沙悟净"]
name_list.extend(temp_list)

# 4.删除
# remove 可以从list删除指定的数据
name_list.remove("lisi")
# pop 默认可以把列表最后一个元素删除,可以指定要删除元素的索引
name_list.pop(4)
# clear 可以清空列表
# name_list.clear()
# del 关键字（delete)删除列表元素，本质是用来将一个变量从内存中删除,如果将变量从内存中删除，则后续代码就不能使用该变量
del name_list[1]


print(name_list)