

def test(num):
    print("在函数内部 %d 对应的内存地址：%d" %(num,id(num)))

    result = "hello"

    print("函数返回值的地址：%d" % id(result))
    return result

a = 10
print("a的内存地址是：%d" %id(a)) # id() 查看变量内存地址

r = test(a)

print("返回值内存地址：%d" %id(r))