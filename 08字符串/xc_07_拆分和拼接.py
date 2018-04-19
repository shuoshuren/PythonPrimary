poem_str = "\t\n登黄鹤楼\t 王之涣 \t 白日依山尽\t\n黄河入海流\t欲穷千里目\n更上一层楼"

print(poem_str)

# 1拆分字符串
poem_list = poem_str.split()
print(poem_list)
# 2.拼接字符串
result = " ".join(poem_list)
print(result)