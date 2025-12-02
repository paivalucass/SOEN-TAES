def catalan_number(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError("Input must be a non-negative integer")

    def factorial(n):
        # Calculate the factorial of a given number
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    result = factorial(2*num) // (factorial(num+1) * factorial(num))
    return result

assert catalan_number(10) == 16796
# Add more test cases to cover a wider range of inputs and edge cases
assert catalan_number(0) == 1
assert catalan_number(1) == 1
assert catalan_number(5) == 42
assert catalan_number(15) == 9694845
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input",
      "Input Data": "num=10",
      "Expected Output": "16796"
    },
    {
      "Test Title": "Negative input",
      "Input Data": "num=-5",
      "Expected Output": "Error: Invalid input, num must be a non-negative integer"
    },
    {
      "Test Title": "Non-integer input",
      "Input Data": "num='abc'",
      "Expected Output": "Error: Invalid input, num must be a non-negative integer"
    },
    {
      "Test Title": "Input 0",
      "Input Data": "num=0",
      "Expected Output": "1"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_catalan_number(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()