def div_sum(a, b):
    sum_a = sum([i for i in range(1, a) if a % i == 0])
    sum_b = sum([i for i in range(1, b) if b % i == 0])
    return sum_a == sum_b
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_sum(36, 57), False)

if __name__ == '__main__':
    unittest.main()