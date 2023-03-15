def hanoi(n, a, b, c):
    # 一共n个盘子，A,B,C 3个柱子
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("moving %s ---> %s" % (a, c))
        hanoi(n - 1, b, a, c)


hanoi(3, 'A', 'B', 'C')
