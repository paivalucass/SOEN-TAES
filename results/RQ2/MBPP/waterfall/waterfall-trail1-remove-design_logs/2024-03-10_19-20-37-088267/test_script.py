from math import factorial
def binomial_coefficient(n, k):
    result = 0
    for i in range(0, k+1):
        result += (factorial(n) / (factorial(i) * factorial(n-i))) * (factorial(n) / (factorial(i) * factorial(n-i)))
    return result
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_Of_product(3), 15)

if __name__ == '__main__':
    unittest.main()