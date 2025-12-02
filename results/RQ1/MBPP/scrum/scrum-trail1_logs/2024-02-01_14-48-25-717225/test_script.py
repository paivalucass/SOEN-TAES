def div_sum(n1, n2):
    sum_divisors_n1 = sum([i for i in range(1, n1) if n1 % i == 0])
    sum_divisors_n2 = sum([i for i in range(1, n2) if n2 % i == 0])
    return sum_divisors_n1 == sum_divisors_n2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_sum(36, 57), False)

if __name__ == '__main__':
    unittest.main()