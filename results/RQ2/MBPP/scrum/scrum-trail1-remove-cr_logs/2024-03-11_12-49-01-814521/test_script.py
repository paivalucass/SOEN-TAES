def div_sum(n):
    divisors_sum = lambda x: sum([i for i in range(1, x) if x % i == 0])
    return divisors_sum(n[0]) == divisors_sum(n[1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(are_equivalent(36, 57), False)

if __name__ == '__main__':
    unittest.main()