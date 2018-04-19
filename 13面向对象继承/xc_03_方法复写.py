class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    # 如果子类中重写了父类方法的实现
    # 则使用子类对象调用方法时，会调用子类方法
    def bark(self):
        print("叫的和神一样")

    def fly(self):
        print("我会飞")


XiaoTianQuan = XiaoTianQuan()
XiaoTianQuan.bark()