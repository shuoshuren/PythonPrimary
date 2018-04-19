
# 1.打开文件
file_read = open("ReadMe")
file_write = open("ReadMe[附件]","w")

# 2.读写
while True:
    # 读取一行内容
    text = file_read.readline()
    # 判断是否读取到内容
    if not text:
        break
    file_write.write(text)

# 3.关闭文件
file_read.close()
file_write.close()

