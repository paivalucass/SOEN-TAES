def binomial_coefficient(n, k):
    if n < k:
        return "Error: n should be greater than or equal to k"
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

def sum_of_product(n):
    if n < 2:
        return "Error: n should be greater than or equal to 2"
    return binomial_coefficient(n+1, 2) * binomial_coefficient(n+2, 2)

import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_Of_product(3), 15)

if __name__ == '__main__':
    unittest.main()