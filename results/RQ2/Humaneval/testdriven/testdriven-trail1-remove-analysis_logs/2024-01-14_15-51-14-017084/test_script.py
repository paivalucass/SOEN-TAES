def is_simple_power(x, n):
    if x <= 0 or n <= 0:
        return False
    return x ** (1 / n) % 1 == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))

if __name__ == '__main__':
    unittest.main()