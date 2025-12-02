def sum(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Both a and b must be positive integers")

    common_divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
    return sum(common_divisors)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(10, 15), 6)

if __name__ == '__main__':
    unittest.main()