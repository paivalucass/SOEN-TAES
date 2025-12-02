import math

def is_simple_power(x, n):
    if n == 0:
        return False

    if x <= 0 or n <= 0:
        return False

    return n ** int(round(math.log(x, n))) == x

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