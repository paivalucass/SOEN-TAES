def truncate_number(number: float) -> float:
    decimal_part = number - int(number)
    return decimal_part
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Positive Floating Point Number",
      "Input Data": "number=3.5",
      "Expected Output": "0.5"
    },
    {
      "Test Title": "Boundary Case - Minimum Value",
      "Input Data": "number=0.0001",
      "Expected Output": "0.0001"
    },
    {
      "Test Title": "Boundary Case - Maximum Value",
      "Input Data": "number=9999999.9999",
      "Expected Output": "0.9999"
    },
    {
      "Test Title": "Invalid Input - Non-numeric",
      "Input Data": "number='abc'",
      "Expected Output": "Error: Non-numeric input"
    },
    {
      "Test Title": "Boundary Case - Negative Floating Point Number",
      "Input Data": "number=-1.234",
      "Expected Output": "0.234"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(truncate_number(3.5), 0.5)

if __name__ == '__main__':
    unittest.main()