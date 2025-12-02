def sumCommonDivisors(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0:
        return "Invalid Input"
    def findCommonDivisors(x, y):
        common_divisors = []
        for i in range(1, min(x, y) + 1):
            if x % i == 0 and y % i == 0:
                common_divisors.append(i)
        return common_divisors

    common_divisors = findCommonDivisors(a, b)
    if len(common_divisors) == 0:
        return 0
    else:
        return sum(common_divisors)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(10, 15), 6)

if __name__ == '__main__':
    unittest.main()