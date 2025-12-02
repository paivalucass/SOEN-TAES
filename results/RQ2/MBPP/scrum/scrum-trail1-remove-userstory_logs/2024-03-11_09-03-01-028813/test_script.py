def even_binomial_Coeff_Sum(n):
    if type(n) != int or n < 0:
        return "Invalid input"
    result = 0
    for i in range(n + 1):
        if i % 2 == 0:
            result += binomial_coefficient(n, i)
    return result

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()