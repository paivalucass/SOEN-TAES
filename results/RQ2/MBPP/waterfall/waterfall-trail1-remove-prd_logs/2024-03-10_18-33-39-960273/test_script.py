def even_binomial_Coeff_Sum(n):
    def binomial_coefficient(n, k):
        res = 1
        if k > n - k:
            k = n - k
        for i in range(k):
            res *= (n - i)
            res //= (i + 1)
        return res

    if n % 2 != 0:
        return 0

    result = 0
    for k in range(n // 2 + 1):
        if k % 2 == 0:
            result += binomial_coefficient(n, k)

    return result
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()