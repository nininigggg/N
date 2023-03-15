"""
列表去重
输入：[10,20,30,30,40,20]
输出：[10,20,30,40]
"""


def get_unique_list(l1):
    result = []
    for i in l1:
        if i not in result:
            result.append(i)
    return result


l1 = [10, 20, 30, 30, 40, 20]
print(f"source list {l1}, unique list:", get_unique_list(l1))

print(f"source list {l1}, unique list:", list(set(l1)))
