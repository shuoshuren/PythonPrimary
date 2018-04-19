class Tool(object):

    # 使用赋值语句定义类属性，
    count = 0

    def __init__(self, name):
        self.name = name
        # 让类属性值+1
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

print(Tool.count)
#不推荐,类属性获取存在向上查找机制
print(tool1.count)
# 使用对象.类属性 = 值赋值语句，只会给对象添加一个属性，而不会影响到类属性的值
tool1.count = 30
print(tool1.count)
print(Tool.count)