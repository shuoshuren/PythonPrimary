class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

# 继承的语法：
# class 类名（父类名）：
#     pass

class Dog(Animal):
    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("喝")
    #
    # def run(self):
    #     print("跑")
    #
    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

# 创建一个狗对象
wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()

xiaotianquan = XiaoTianQuan();
xiaotianquan.eat()
xiaotianquan.bark()
xiaotianquan.fly()