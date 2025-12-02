def closest_num(N):
    if N <= 0:
        return "Error: Please provide a positive integer."

    closest_smaller = N - 1
    return closest_smaller

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Positive Integer Input",
      "Input Data": "parameter1=10",
      "Expected Output": "9"
    },
    {
      "Test Title": "Negative Integer Input",
      "Input Data": "parameter1=-6",
      "Expected Output": "Error Message"
    },
    {
      "Test Title": "Zero Input",
      "Input Data": "parameter1=-1",
      "Expected Output": "-2"
    },
    {
      "Test Title": "Large Integer Input",
      "Input Data": "parameter1=9999998",
      "Expected Output": "9999997"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()