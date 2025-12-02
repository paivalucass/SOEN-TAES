def sum_of_factors(n):
    if not isinstance(n, int) or n < 1:
        return "Invalid input"
    
    total_sum = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            total_sum += i
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sumofFactors(18), 26)

if __name__ == '__main__':
    unittest.main()