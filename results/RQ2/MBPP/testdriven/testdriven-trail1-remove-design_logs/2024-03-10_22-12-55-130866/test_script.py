def binomial_coefficient(n, k):
    if n < 0 or k < 0:
        return "Invalid input"
    if k > n:
        return 0
    result = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

def sum_of_product(n):
    result = 0
    for i in range(n):
        result += binomial_coefficient(n, i) * binomial_coefficient(n, i + 1)
    return result

# Test case
assert sum_of_product(3) == 15
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(binomial_Coeff(3), 15)

if __name__ == '__main__':
    unittest.main()