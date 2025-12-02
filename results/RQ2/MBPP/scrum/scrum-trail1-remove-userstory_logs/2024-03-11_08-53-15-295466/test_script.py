def power(a, b):
    if b < 0:
        raise ValueError("The power cannot be a negative number.")
    result = 1
    base = a
    while b > 0:
        if b % 2 == 1:
            result *= base
        base *= base
        b //= 2
    return result
import unittest

class Test(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3, 4), 81)

if __name__ == '__main__':
    unittest.main()