def even_binomial_Coeff_Sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Error Message"
    memo = {}
    def factorial(num):
        if num in memo:
            return memo[num]
        if num == 0:
            return 1
        else:
            result = num * factorial(num - 1)
            memo[num] = result
            return result
    def binomial_coefficient(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))
    sum_even_binomial = 0
    for r in range(n + 1):
        if r % 2 == 0:
            sum_even_binomial += binomial_coefficient(n, r)
    return sum_even_binomial
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()