# 函数递归：
# 函数在内部调用自己
# 代码特点：
# 函数内部的代码是相同的，只是针对参数不同，处理的结果不同，当参数满足一个条件时，函数就不在执行

def sum_num(num):

    print(num)
    if num == 1:
        return
    sum_num(num-1)

sum_num(6)