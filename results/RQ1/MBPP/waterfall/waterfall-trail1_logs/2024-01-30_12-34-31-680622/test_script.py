def sum(a, b):
    if a <= 0 or b <= 0:
        return 0

    common_divisors_sum = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors_sum += i

    return common_divisors_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(10, 15), 6)

if __name__ == '__main__':
    unittest.main()