def even_binomial_Coeff_Sum(n):
    if n < 0:
        return "Error"
    elif n == 0:
        return 0
    else:
        sum = 0
        for i in range(n + 1):
            if i % 2 == 0:
                sum += binomialCoefficient(n, i)
        return sum

def binomialCoefficient(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input test",
      "Input Data": "parameter1=4",
      "Expected Output": "8"
    },
    {
      "Test Title": "Input validation test",
      "Input Data": "parameter1=-4",
      "Expected Output": "Error"
    },
    {
      "Test Title": "Edge case test for 0",
      "Input Data": "parameter1=0",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_even_binomial_Coeff_Sum(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()