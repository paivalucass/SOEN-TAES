def is_multiply_prime(a):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_prime_factors(n):
        factors = []
        for i in range(2, n+1):
            if n % i == 0 and is_prime(i):
                factors.append(i)
        return factors

    if a < 2:
        return False
    
    prime_factors = find_prime_factors(a)
    if len(prime_factors) == 3:
        return True
    else:
        return False
  
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test for prime number function",
      "Input Data": "Number: -7",
      "Expected Output": "False"
    },
    {
      "Test Title": "Test for prime number function",
      "Input Data": "Number: 0",
      "Expected Output": "False"
    },
    {
      "Test Title": "Test for prime number function",
      "Input Data": "Number: 101",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for multiplication function",
      "Input Data": "Number: 99",
      "Expected Output": "True"
    },
    {
      "Test Title": "Test for multiplication function",
      "Input Data": "Number: 97",
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