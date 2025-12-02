def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    a, b = 1, 1
    count = 1
    while True:
        if is_prime(a) and count == n:
            return a
        a, b = b, a + b
        count += 1

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input Case",
      "Input Data": "n=1",
      "Expected Output": "2"
    },
    {
      "Test Title": "Valid Input Case",
      "Input Data": "n=2",
      "Expected Output": "3"
    },
    {
      "Test Title": "Valid Input Case",
      "Input Data": "n=3",
      "Expected Output": "5"
    },
    {
      "Test Title": "Valid Input Case",
      "Input Data": "n=4",
      "Expected Output": "13"
    },
    {
      "Test Title": "Valid Input Case",
      "Input Data": "n=5",
      "Expected Output": "89"
    },
    {
      "Test Title": "Invalid Input Case",
      "Input Data": "n=0",
      "Expected Output": "Invalid Input"
    },
    {
      "Test Title": "Edge Case",
      "Input Data": "n=100",
      "Expected Output": "354224848179261915075"
    },
    {
      "Test Title": "Negative Test Case",
      "Input Data": "n=-1",
      "Expected Output": "Invalid Input"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

if __name__ == '__main__':
    unittest.main()