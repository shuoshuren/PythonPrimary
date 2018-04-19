
xiaoming_dict = {"name": "小明"}
# 取值
print(xiaoming_dict["name"])
# 新增/修改
# 如果key不存在，则新增键值对，如果key存在，则修改键值对
xiaoming_dict["age"] = 18
xiaoming_dict["name"] = "小小明"
# 删除
# xiaoming_dict.pop("name")
# 统计键值对数量
print(len(xiaoming_dict))
# 合并字典,如果被合并的字典包含已存在的键值对，则会覆盖原有的键值对
temp_dict = {"height":180,
             "age":30}
xiaoming_dict.update(temp_dict)

# 清空字典
# xiaoming_dict.clear()
print(xiaoming_dict)

# 循环遍历,key是每次循环中，获取到的键值对的key
for key in xiaoming_dict:
    print("%s--%s" %(key,xiaoming_dict[key]))
