"""
count:

index:

"""
info_tuple = ("zhangsan",18,12.5,"zhangsan")
# 取值和取索引
print(info_tuple[0])
print(info_tuple.index(18))
# 统计计数
print(info_tuple.count("zhangsan"))

# 元组的遍历
for info in info_tuple:
    print(info)