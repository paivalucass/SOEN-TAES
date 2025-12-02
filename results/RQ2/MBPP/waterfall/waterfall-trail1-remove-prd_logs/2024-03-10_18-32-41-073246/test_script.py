def count_Primes_nums(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    count_of_primes = 0
    # Sieve of Eratosthenes algorithm implementation
    prime_flags = [True] * n
    prime_flags[0:2] = [False, False]  # 0 and 1 are not prime numbers
    
    for i in range(2, int(n ** 0.5) + 1):
        if prime_flags[i]:
            for j in range(i * i, n, i):
                prime_flags[j] = False
    
    count_of_primes = sum(prime_flags)
    
    return count_of_primes

# Test Cases:
{
  "requirement analysis": "The function should take a non-negative integer input and return the number of prime numbers less than the given input.",
  "test_cases": [
    {
      "Test Title": "Valid input",
      "Input Data": "n=5",
      "Expected Output": "2"
    },
    {
      "Test Title": "Edge case: input is 0",
      "Input Data": "n=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large input value",
      "Input Data": "n=1000",
      "Expected Output": "<expected_output>"
    },
    {
      "Test Title": "Negative input value",
      "Input Data": "n=-5",
      "Expected Output": "<expected_output>"
    },
    {
      "Test Title": "Invalid input: non-integer input",
      "Input Data": "n='abc'",
      "Expected Output": "<expected_output>"
    },
    {
      "Test Title": "Boundary condition: smallest possible input value",
      "Input Data": "n=1",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Primes_nums(5), 2)

if __name__ == '__main__':
    unittest.main()