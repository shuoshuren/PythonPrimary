# 1.打开
# "r" 只读,默认的方式
# "w" 以只写的方式覆盖原有的内容
# "a" 追加的方式打开文件
file = open("ReadMe","a")

# 2.写入文件
file.write("中国")

# 3.关闭
file.close()