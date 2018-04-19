
# 1.打开文件
file = open("ReadMe")

# 读取文件
# read()读取完成后,文件指针会移动到读取内容的末尾,默认会读取所有的内容

# text = file.read()
# print(text)
print("-"*50)

# readline() 一次读取一行内容
while True:
    text_line = file.readline()
    # 判断是否读取到内容
    if not text_line:
        break
    print(text_line)


# 关闭文件
file.close()