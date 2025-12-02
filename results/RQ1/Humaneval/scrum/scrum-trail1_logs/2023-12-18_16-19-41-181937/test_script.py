def largest_prime_factor(n: int):
    if n <= 1 or is_prime(n):
        return None
    
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
# Test Cases:
{
  "requirement analysis": "analysis",
  "test_cases": [
    {
      "Test Title": "positive_input_test",
      "Input Data": "parameter1=13195",
      "Expected Output": "29"
    },
    {
      "Test Title": "large_input_test",
      "Input Data": "parameter1=600851475143",
      "Expected Output": "6857"
    },
    {
      "Test Title": "negative_input_test",
      "Input Data": "parameter1=10",
      "Expected Output": "5"
    },
    {
      "Test Title": "zero_input_test",
      "Input Data": "parameter1=0",
      "Expected Output": "None"
    },
    {
      "Test Title": "empty_input_test",
      "Input Data": "parameter1=",
      "Expected Output": "None"
    },
    {
      "Test Title": "very_large_input_test",
      "Input Data": "parameter1=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "Expected Output": "None"
    },
    {
      "Test Title": "prime_factorization_of_large_number",
      "Input Data": "parameter1=600851475143",
      "Expected Output": "6857"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()