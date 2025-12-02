def newman_prime(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    count = 2
    num = 5
    while count < n:
        if is_prime(num):
            count += 1
        num += 2
    return num


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_newman_prime(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()