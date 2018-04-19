
def print_line(char ,times):
    """
    打印一条分割线
    :param char: 线的字符
    :param times: 字符重复次数
    :return:
    """
    print(char * times)


def print_lines(char,times,cols):
    """
    打印多条分割线
    :param char:
    :param times:
    :param cols:
    :return:
    """
    col = 0
    while col<cols:
        print_line(char,times)
        col += 1

