def largest_divisor(n: int) -> int:
    if n <= 0:
        raise ValueError("Input should be a positive integer")

    if n == 1:
        return 1

    largest = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            largest = max(largest, i, n//i)

    return largest

# Test Cases:
{
  "requirement analysis": "analysis",
  "test_cases": [
    {
      "Test Title": "positive integer input",
      "Input Data": "parameter1=15",
      "Expected Output": "5"
    },
    {
      "Test Title": "negative integer input",
      "Input Data": "parameter1=-15",
      "Expected Output": "-5"
    },
    {
      "Test Title": "zero input",
      "Input Data": "parameter1=0",
      "Expected Output": "No output"
    },
    {
      "Test Title": "large input value",
      "Input Data": "parameter1=1000000",
      "Expected Output": "10000"
    },
    {
      "Test Title": "maximum possible input value",
      "Input Data": "parameter1=2147483647",
      "Expected Output": "1"
    },
    {
      "Test Title": "minimum possible input value",
      "Input Data": "parameter1=-2147483648",
      "Expected Output": "-1"
    },
    {
      "Test Title": "non-integer input",
      "Input Data": "parameter1=15.5",
      "Expected Output": "Invalid input"
    },
    {
      "Test Title": "special character input",
      "Input Data": "parameter1=abc",
      "Expected Output": "Invalid input"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_divisor(15), 5)

if __name__ == '__main__':
    unittest.main()