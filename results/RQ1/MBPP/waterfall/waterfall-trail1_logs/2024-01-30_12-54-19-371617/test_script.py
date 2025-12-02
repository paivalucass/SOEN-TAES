def even_binomial_Coeff_Sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Please enter a positive integer value for n"
    
    sum_even = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum_even += binomial_coefficient(n, i)
    
    return sum_even


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def binomial_coefficient(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)) if n >= k >= 0 else 0)
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()