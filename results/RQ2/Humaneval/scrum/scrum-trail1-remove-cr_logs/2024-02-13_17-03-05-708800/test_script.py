def is_simple_power(x, n):
    if x == 1:
        return n == 1
    power = 1
    while power < x:
        power *= n
    return power == x
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