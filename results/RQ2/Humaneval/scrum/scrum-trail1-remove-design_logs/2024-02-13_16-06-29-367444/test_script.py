def fib(n: int):
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input Test",
      "Input Data": "n=10",
      "Expected Output": "55"
    },
    {
      "Test Title": "Boundary Input Test",
      "Input Data": "n=1",
      "Expected Output": "1"
    },
    {
      "Test Title": "Large Input Test",
      "Input Data": "n=50",
      "Expected Output": "12586269025"
    },
    {
      "Test Title": "Negative Input Test",
      "Input Data": "n=-5",
      "Expected Output": "Invalid input"
    },
    {
      "Test Title": "Edge Case Test",
      "Input Data": "n=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Error Handling Test",
      "Input Data": "n='abc'",
      "Expected Output": "Invalid input"
    }
  ]
}
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fib_10(self):
        self.assertEqual(fib(10), 55)

    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_8(self):
        self.assertEqual(fib(8), 21)

if __name__ == '__main__':
    unittest.main()