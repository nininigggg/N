import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s spend_time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper


@cal_time
def linear_search(li, val):
    for index, value in enumerate(li):
        if value == val:
            return index
    else:
        return None


# 也可以使用range
# def linear_search(li, val):
#     for i in range(len(li)):
#         if li[i] == val:
#             return i
#     else:
#         return None
@cal_time
def binary_search(li, val):
    left = 0  # 左指针
    right = len(li) - 1  # 右指针
    while left <= right:  # 存在候选区
        mid = (left + right) // 2  # 取整数
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            left = mid + 1  # 候选区右移，在mid右侧
        else:  # li[mid] > val 候选区左移，在mid左侧
            right = mid - 1
    else:
        return None


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li = list(range(10000))
print(linear_search(li, 7987))
print(binary_search(li, 7987))
