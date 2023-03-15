"""
原始：[3,4,5,8,18,35]
移除：[3,18]
return:[4,5,8,35]
"""


def remove_element_from_list(l1, l2):
    # result = []
    # for i in l1:
    #     if i not in l2:
    #         result.append(i)
    # return result
    for i in l2:
        l1.remove(i)
    return l1


l1 = [3, 4, 5, 8, 18, 35]
l2 = [3, 18]
print(f"from{l1}，remove{l2}, result:", remove_element_from_list(l1, l2))

l1 = [3, 4, 5, 8, 18, 35]
l2 = [3, 18]
data = [i for i in l1 if i not in l2]
print(f"from{l1}，remove{l2}, result:", data)
