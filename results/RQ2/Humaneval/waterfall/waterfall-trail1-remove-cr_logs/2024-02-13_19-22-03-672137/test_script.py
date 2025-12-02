def is_simple_power(x, n):
    if not isinstance(x, int) or not isinstance(n, int) or x <= 0 or n <= 0:
        return False

    if x == 1 or n == 1:
        return True

    return x == n**int(x/n)
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