def is_multiply_prime(a):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_prime_factors(num):
        factors = []
        for i in range(2, num + 1):
            while num % i == 0:
                factors.append(i)
                num = num / i
        return factors

    if a < 2:
        return False
    factors = find_prime_factors(a)
    if len(factors) == 3 and all(is_prime(f) for f in factors):
        return True
    else:
        return False
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input: Multiplication of 3 prime numbers",
      "Input Data": "parameter1=30, parameter2='2 * 3 * 5'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Valid Input: Not a Multiplication of 3 prime numbers",
      "Input Data": "parameter1=21, parameter2='3 * 7'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Edge Case: Number less than 2",
      "Input Data": "parameter1=1, parameter2=''",
      "Expected Output": "False"
    },
    {
      "Test Title": "Edge Case: Number greater than 100",
      "Input Data": "parameter1=101, parameter2=''",
      "Expected Output": "False"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_multiply_prime(30), True)

if __name__ == '__main__':
    unittest.main()