def even_binomial_Coeff_Sum(n):
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num-1)

    def binomial_coefficient(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    result = 0
    for k in range(n + 1):
        if k % 2 == 0:
            result += binomial_coefficient(n, k)

    return result
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()