"""过滤素数"""


def is_prime(number):
    if number == 2:
        return True
    for idx in range(2, number):
        if number % idx == 0:
            return False
    return True


def print_primes(begin, end):
    for number in range(begin, end+1):
        if is_prime(number):
            print(f"{number} is a prime.")


def test_primes():
    print_primes(11, 25)
