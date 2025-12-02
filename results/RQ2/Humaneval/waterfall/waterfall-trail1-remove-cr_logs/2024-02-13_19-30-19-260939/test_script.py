def x_or_y(n, x, y):
    if n < 2:
        return y
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return y
    return x
import unittest

class Test(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_non_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

if __name__ == '__main__':
    unittest.main()