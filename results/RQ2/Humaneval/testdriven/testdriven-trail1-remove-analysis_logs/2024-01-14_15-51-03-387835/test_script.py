def is_multiply_prime(a):
    if a < 2:
        return False
    factors = []
    for i in range(2, a):
        while a % i == 0:
            factors.append(i)
            a = a / i
    if len(factors) == 3:
        return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_multiply_prime(30), True)
        self.assertEqual(is_multiply_prime(10), False)

if __name__ == '__main__':
    unittest.main()