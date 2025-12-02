def is_simple_power(x, n):
    if x < 1 or n < 1:
        return False
    if x == 1:
        return True
    for i in range(2, int(x**(1/n)) + 2):
        power = n**i
        if x == power:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test_is_simple_power(self):
        self.assertEqual(is_simple_power(1, 4), True)
        self.assertEqual(is_simple_power(2, 2), True)
        self.assertEqual(is_simple_power(8, 2), True)
        self.assertEqual(is_simple_power(3, 2), False)
        self.assertEqual(is_simple_power(3, 1), False)
        self.assertEqual(is_simple_power(5, 3), False)

if __name__ == '__main__':
    unittest.main()