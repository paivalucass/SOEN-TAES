def power(a, b):
    if a < 0:
        raise ValueError("'a' should be a positive integer")
    if b < 0:
        raise ValueError("'b' should be a positive integer")

    if b == 0:
        return 1

    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2

    return result
import unittest

class Test(unittest.TestCase):
    def test_power_function(self):
        self.assertEqual(power(3, 4), 81)

if __name__ == '__main__':
    unittest.main()