poem = ["\t\n登黄鹤楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

# lstrip:去除左边的字符串
# rstrip:去除右边的字符串
# strip:去除左右的字符串
for poem_str in poem:
    print("|%s|" %poem_str.strip().center(6," "))