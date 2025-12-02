def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(num, x, y):
    if not isinstance(num, int) or num <= 0:
        raise ValueError("n must be a positive integer")

    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("x and y must be numbers")

    if is_prime(num):
        return x
    else:
        return y
import unittest

class Test(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_not_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

if __name__ == '__main__':
    unittest.main()