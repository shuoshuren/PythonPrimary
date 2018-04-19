
# 导入随机包
import random

# 从控制台输入要出的拳
player = int(input("请输入石头(1),剪刀(2),布（3）："))

# 电脑出拳
computer = random.randint(1,3)

print("你出的是：%d 电脑出的是：%d" %(player,computer))

# 比较
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("电脑弱爆了")
elif player == computer:
    print("不分胜负，继续")
else:
    print("下次一定赢你")

