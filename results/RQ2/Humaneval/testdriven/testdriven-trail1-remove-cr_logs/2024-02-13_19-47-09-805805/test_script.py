def is_simple_power(x, n):
    return x > 0 and n > 0 and (x == 1 or (x % n == 0 and (x / n) % n == 0))
import unittest

class Test(unittest.TestCase):
    def test_is_simple_power(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))

if __name__ == '__main__':
    unittest.main()