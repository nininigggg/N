"""
计算给定范围内的偶数
输入：begin :4, end: 15
[4,6,8,10,12,14]
"""


def get_even_numbers(begin, end):
    result = []
    for i in range(begin, end):
        if i % 2 == 0:
            result.append(i)
    return result


begin = 4
end = 15
print(f"begin={begin}, end={end}, even numbers:", get_even_numbers(4, 15))

# 列表表达式
data = [i for i in range(begin, end) if i % 2 == 0]
print(f"begin={begin}, end={end}, even numbers:", data)