
# 在参数后面添加赋值语句，可以指定参数的默认值
def print_info(name,gender = True):
    """

    :param name: 姓名
    :param gender: 性别 true男生，false女生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" %(name,gender_text))

print_info("小明",True)
print_info("老王")
print_info("小妹",False)
