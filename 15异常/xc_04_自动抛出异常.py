# 主动抛出异常：
# 1.创建一个Exception的对象
# 2.使用raise关键字抛出异常对象


def input_password():

    # 1.提示用户输入密码
    pwd = input("请输入密码：")

    # 2.判断密码长度>=8，返回用户输入的密码
    if len(pwd)>=8:
        return pwd
    # 3.如果<8，主动抛出异常
    else:
        # 1.创建异常对象
        ex = Exception("密码长度不够8位")
        # 2.主动抛出异常
        raise ex


try:
    print(input_password())
except Exception as result:
    print(result)