def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test2(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

if __name__ == '__main__':
    unittest.main()