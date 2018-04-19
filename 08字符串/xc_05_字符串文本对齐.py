poem = ["登黄鹤楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
# center:居中对齐
# ljust:向左对齐
# rjust:向右对齐
for poem_str in poem:
    print("|%s|" %poem_str.rjust(6," "))