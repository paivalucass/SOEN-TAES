def sum_of_factors(n):
    if n <= 0:
        return "Input number should be a positive integer"
    sum_of_factors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum_of_factors += i
            if i != n // i and (n // i) % 2 == 0:
                sum_of_factors += n // i
    return sum_of_factors
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sumofFactors(18), 26)

if __name__ == '__main__':
    unittest.main()