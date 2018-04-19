def measure():
    """
    测量温度
    :return:
    """
    print("测量开始")
    temp = 37
    wetness = 50
    print("测量结束")

    # 元组-可以包含多个数据，因此可以使用元组一次返回多个数据
    # 如果函数返回类型是元组，小括号可以省略
    # return (temp,wetness)
    return temp,wetness


measure_result = measure()
print(measure_result)

print(measure_result[0])
print(measure_result[1])

# 如果函数返回类型是元组，同时希望单独处理元组中的元素，可以使用多个变量一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数应该和元组中元素的个数相同
gl_temp,gl_wetness = measure()
# print("temp:%d wetness：%d" %(gl_temp,gl_wetness))