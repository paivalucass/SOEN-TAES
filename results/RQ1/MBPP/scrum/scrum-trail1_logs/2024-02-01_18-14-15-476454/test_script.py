def count_Primes_nums(n):
    # Function to count the number of prime numbers less than the given non-negative number
    # Returns the count of prime numbers

    if n < 2:
        return 0  # There are no prime numbers less than 2

    primes = [True] * n
    primes[0], primes[1] = False, False  # 0 and 1 are not prime numbers

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i*i:n:i] = [False] * len(primes[i*i:n:i])  # Mark multiples of i as non-prime

    return sum(primes)  # Return the count of prime numbers

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input test case",
      "Input Data": "parameter1=5",
      "Expected Output": "2"
    },
    {
      "Test Title": "Edge case test case",
      "Input Data": "parameter1=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Invalid input test case",
      "Input Data": "parameter1=-5",
      "Expected Output": "Invalid input"
    }
    ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Primes_nums(5), 2)

if __name__ == '__main__':
    unittest.main()