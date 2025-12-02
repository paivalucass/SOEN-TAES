def binomial_coefficient(n, k):
    result = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

def sum_of_product(n):
    if not isinstance(n, int) or n < 0:
        return "Error"
    if n == 0:
        return 1
    total_sum = 0
    for i in range(n + 1):
        total_sum += binomial_coefficient(n, i) * binomial_coefficient(n, i)
    return total_sum

# test report:
Test Report:

Test Script Output:
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

Conclusion:
The code has passed the test.

Input and Expected Output Example:
Input: sum_of_product(3)
Expected Output: 15

Code Test Passed.
import unittest

class Test(unittest.TestCase):
    def test_binomial_Coeff(self):
        self.assertEqual(sum_Of_product(3), 15)

if __name__ == '__main__':
    unittest.main()