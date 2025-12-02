def even_binomial_Coeff_Sum(n):
    result = 0
    for i in range(n+1):
        if i % 2 == 0:
            result += (2 ** i)
    return result
import unittest

class Test(unittest.TestCase):
    def test_even_binomial_Coeff_Sum(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()