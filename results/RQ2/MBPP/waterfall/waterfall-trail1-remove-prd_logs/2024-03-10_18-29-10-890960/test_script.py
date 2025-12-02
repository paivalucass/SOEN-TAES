def find_common_divisors(x, y):
    common_divisors = []
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            common_divisors.append(i)
    return common_divisors


def sum_of_common_divisors(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive integers.")

    common_divisors = find_common_divisors(a, b)
    result = sum(common_divisors)

    if len(common_divisors) == 0:
        return 0

    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(10, 15), 6)

if __name__ == '__main__':
    unittest.main()