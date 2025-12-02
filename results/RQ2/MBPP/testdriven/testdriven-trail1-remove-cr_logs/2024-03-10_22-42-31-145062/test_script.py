def sumOfEvenFactors(n):
    if n <= 0:
        return 0
    sum_even_factors = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            sum_even_factors += i
    return sum_even_factors
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sumofFactors(18), 26)

if __name__ == '__main__':
    unittest.main()