def binomial_coeff(n, k):
    if not isinstance(n, int) or n < 0 or not isinstance(k, int) or k < 0 or k > n:
        return "Invalid input: n and k must be non-negative integers and k must be less than or equal to n"
    
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * factorial(num-1)
    
    def binomial_coef(n, k):
        return factorial(n) / (factorial(k) * factorial(n - k))
    
    result = 0
    for i in range(n):
        result += binomial_coef(n, i) * binomial_coef(n, i+1)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(binomial_Coeff(3), 15)

if __name__ == '__main__':
    unittest.main()