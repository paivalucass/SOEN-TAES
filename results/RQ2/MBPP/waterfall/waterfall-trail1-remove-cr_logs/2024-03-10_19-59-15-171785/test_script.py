def even_binomial_Coeff_Sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    
    if n == 1:
        return 1
    
    res = 1
    
    for i in range(1, n+1):
        if (n - i + 1) % i == 0:
            res += (n - i + 1) // i
    
    return res

import unittest

class Test(unittest.TestCase):
    def test_even_binomial_Coeff_Sum(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()