import math
import unittest

def binomial_Coeff(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def sum_Of_product(n):
    result = 0
    for i in range(n):
        result += binomial_Coeff(n, i) * binomial_Coeff(n, i + 1)
    return result

class TestBinomialCoeff(unittest.TestCase):
    def test_sum_Of_product(self):
        self.assertEqual(sum_Of_product(3), 15)

if __name__ == '__main__':
    unittest.main()
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_Of_product(3), 15)

if __name__ == '__main__':
    unittest.main()