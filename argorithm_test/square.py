"""求n个数平方和"""


def sum_of_square(n):
    result = 0
    for number in (1, n + 1):
        result += number * number
    return result


def sum_of_squares(n):
    return sum(x ** 2 for x in range(1, n + 1))


def test_square():
    print("sum of square 3:", sum_of_square(3))
    print("sum of square 5:", sum_of_square(5))
    print("sum of squares 3:", sum_of_squares(3))
    print("sum of squares 5:", sum_of_squares(5))
