def newman_prime(n):
    if n <= 0:
        return 'Invalid input'
    if n == 1:
        return 2
    count = 1
    num = 1
    while count < n:
        num += 1
        if is_prime(num) and is_newman_shanks_williams_prime(num):
            count += 1
    return num


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_newman_shanks_williams_prime(num):
    return (num - 1) % (num ** 2) == 0

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()