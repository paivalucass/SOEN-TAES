def is_simple_power(x, n):
    if not isinstance(x, int) or not isinstance(n, int) or x < 0 or n <= 1:
        return False
    if x == 0:
        return False
    if n == 0 or n == 1:
        return True
    while x % n == 0:
        x //= n
    return x == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_simple_power(1, 4), True)
        self.assertEqual(is_simple_power(2, 2), True)
        self.assertEqual(is_simple_power(8, 2), True)
        self.assertEqual(is_simple_power(3, 2), False)
        self.assertEqual(is_simple_power(3, 1), False)
        self.assertEqual(is_simple_power(5, 3), False)

if __name__ == '__main__':
    unittest.main()