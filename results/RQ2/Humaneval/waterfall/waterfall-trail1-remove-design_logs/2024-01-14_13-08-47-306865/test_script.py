def triangle_area(a, h):
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        return "Error"
    if a <= 0 or h <= 0:
        return "Invalid input: 'a' and 'h' must be positive numbers"
    return 0.5 * a * h

# Test for boundary cases
print(triangle_area(0, 5))  # Output: Invalid input: 'a' and 'h' must be positive numbers
print(triangle_area(5, -10))  # Output: Invalid input: 'a' and 'h' must be positive numbers
print(triangle_area(1000000, 1000000))  # Output: 500000000.0

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input",
      "Input Data": "a=5, h=3",
      "Expected Output": "7.5"
    },
    {
      "Test Title": "Zero input",
      "Input Data": "a=0, h=3",
      "Expected Output": "0"
    },
    {
      "Test Title": "Negative input",
      "Input Data": "a=-5, h=3",
      "Expected Output": "Error"
    },
    {
      "Test Title": "Extreme large input",
      "Input Data": "a=999999, h=999999",
      "Expected Output": "Error"
    },
    {
      "Test Title": "Float input",
      "Input Data": "a=2.5, h=3.1",
      "Expected Output": "3.75"
    },
    {
      "Test Title": "Invalid input data",
      "Input Data": "a='abc', h='xyz'",
      "Expected Output": "Error"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()