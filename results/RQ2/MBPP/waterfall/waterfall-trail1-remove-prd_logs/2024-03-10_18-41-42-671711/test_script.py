def last_Digit_Factorial(n):
    def factorial(n, memo):
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return 1
        memo[n] = n * factorial(n-1, memo)
        return memo[n] % 10
    memo = {}
    result = factorial(n, memo)
    return result
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

if __name__ == '__main__':
    unittest.main()