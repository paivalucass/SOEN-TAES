def newman_prime(n):
    if n == 1:
        return 2
    count = 1
    num = 3
    while count < n:
        num += 2
        if is_prime(num) and is_newman_shanks_williams(num):
            count += 1
    return num


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_newman_shanks_williams(num):
    if num == 2:
        return True
    prev = 1
    curr = 1
    for _ in range(3, num + 1):
        next_num = prev + curr
        prev = curr
        curr = next_num
    return curr % num == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()