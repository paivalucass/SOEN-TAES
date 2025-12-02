def centered_hexagonal_number(n):
    if not isinstance(n, int) or n < 1:
        return "Error"
    elif n == 1:
        return 1
    else:
        return 3*n*n - 3*n + 1

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input",
      "Input Data": "parameter1=1",
      "Expected Output": "1"
    },
    {
      "Test Title": "Valid Input",
      "Input Data": "parameter1=100",
      "Expected Output": "19201"
    },
    {
      "Test Title": "Valid Input",
      "Input Data": "parameter1=10000000",
      "Expected Output": "333333333333333333"
    },
    {
      "Test Title": "Input Validation",
      "Input Data": "parameter1=abc",
      "Expected Output": "Error"
    },
    {
      "Test Title": "Performance Test",
      "Input Data": "parameter1=1000000000",
      "Expected Output": "Large Number"
    },
    {
      "Test Title": "Different Environment",
      "Input Data": "parameter1=10",
      "Expected Output": "271"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()