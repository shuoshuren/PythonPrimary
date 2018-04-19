
# 九九乘法表
row = 1

while row <= 9:
    col = 1
    while col <= row:
        # print("*",end="")
        print("%d*%d=%d\t" %(col,row,col*row) ,end="")
        col += 1
    print("")

    row += 1
