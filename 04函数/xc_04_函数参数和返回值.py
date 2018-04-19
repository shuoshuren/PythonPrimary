"""
函数参数：
在函数名的后面的小括号内部填写参数，在多个参数之间使用，分割

返回值：
在函数中使用return关键字可以返回给调用者的一个结果
"""


def sum_2_num(num1,num2):
    """
    计算两个数字的求和
    :param num1:加数1
    :param num2:加数2
    :return:求和结果
    """
    result = num1+num2
    return result


sum_result = sum_2_num(10,-50)
print(sum_result)