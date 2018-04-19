def say_hello():
    print("测试模块2")


class Cat(object):
    pass


def main():
    print(__name__)

    say_hello()

if __name__ == "__main__":

    main()

