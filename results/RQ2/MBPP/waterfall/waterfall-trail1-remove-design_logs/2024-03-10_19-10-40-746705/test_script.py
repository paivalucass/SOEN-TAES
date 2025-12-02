import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def newman_prime(n):
    if n <= 0:
        return "Invalid input"
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()