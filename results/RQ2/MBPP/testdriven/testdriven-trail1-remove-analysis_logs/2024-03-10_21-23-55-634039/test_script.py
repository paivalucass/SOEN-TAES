from math import comb

def sum_Of_product(n):
    result = 0
    for i in range(n):
        result += comb(n, i) * comb(n, i+1)
    return result

assert sum_Of_product(3) == 15
import unittest

class Test(unittest.TestCase):
    def test_sum_Of_product(self):
        self.assertEqual(sum_Of_product(3), 15)

if __name__ == '__main__':
    unittest.main()