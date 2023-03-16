import random


def bubble_sort(li):
    for i in range(len(li) - 1):  # i趟
        exchange = False  # 表示本趟是否操作排序
        for j in range(len(li) - 1 - i):  # 每一趟比较无序的区域，第i趟会产生i个有序的数
            if li[j] > li[j + 1]:  # 当前数和后一个做对比
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return  # 如果当前趟内每个数的对比发现没有移动，则已完成排序


li = [8, 7, 9, 5, 4, 2, 6, 1, 3]
# li1 = [random.randint(0, 100) for i in range(100)]
bubble_sort(li)
print(li)
