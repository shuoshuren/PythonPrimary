class Woman:

    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部可以访问到私有属性
        print("%s的年龄是：%d" %(self.name,self.__age))


xiaofang = Woman("小芳")
# 私有属性不能在外界访问
# print(xiaofang.__age)
# 私有方法不能在外界访问
# xiaofang.__secret()