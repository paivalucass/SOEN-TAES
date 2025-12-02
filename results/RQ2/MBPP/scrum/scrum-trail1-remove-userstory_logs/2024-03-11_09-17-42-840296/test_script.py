def binomial_Coeff(n, k):
    result = 1
    for i in range(1, k+1):
        result *= (n - i + 1)
        result //= i
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_Of_product(3), 15)

if __name__ == '__main__':
    unittest.main()