# 捕获错误类型：针对不同类型的异常，做出不同响应
# 完整语法如下：
# try:
#     将要执行的代码
#     pass
# except 错误类型1:
#     针对错误类型1，要执行的代码
# except (错误类型2，错误类型3)：
#     针对错误类型2,3要执行的代码
# except Exception as result:
#      print("未知错误%s" %result)
# else:
#     没有异常才会执行的代码
#     pass
# finally:
#     无论是否有异常，都会执行的代码

try:
    num = int(input("请输入一个整数："))

    result = 8/num

    print(result)
except ValueError:
    print("请输入一个整数")
# except ZeroDivisionError:
#     print("不能输入0")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("正确执行")
finally:
    print("无论是否出现错误都会执行")
