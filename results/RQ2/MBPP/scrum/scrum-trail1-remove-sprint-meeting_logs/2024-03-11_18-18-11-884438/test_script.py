def divisor(n):
    if not isinstance(n, int) or n <= 0:
        return "Input must be a positive integer"
    if n == 1:
        return 1
    divisors = 0
    limit = int(n**0.5) + 1
    for i in range(1, limit):
        if n % i == 0:
            divisors += 2
    if limit**2 == n:
        divisors -= 1
    return divisors

assert divisor(15) == 4
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisor(15), 4)

if __name__ == '__main__':
    unittest.main()