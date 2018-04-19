# 1.判断空白字符
space_str = " \t \n \r"
print(space_str.isspace())

# 2.判断字符串中只包含数字
# 1>都不能判断小数
# num_str = "1"
# isdecimal 只判断数字
# 2>Unicode字符串
# num_str = "\u00B2"
# isdigit 能够判断数字和Unicode字符

num_str = "一十二"
# isnumeric 能够判断数字和Unicode字符,中文数字
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())