def sum_of_common_divisors(a, b):
    if a <= 0 or b <= 0:
        return 0

    common_divisors = [i for i in range(1, min(a,b)+1) if a % i == 0 and b % i == 0]

    return sum(common_divisors)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(10, 15), 6)

if __name__ == '__main__':
    unittest.main()