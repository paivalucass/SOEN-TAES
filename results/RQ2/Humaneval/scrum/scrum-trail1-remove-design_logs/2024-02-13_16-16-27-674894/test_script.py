def choose_num(x, y):
    largest_even = -1
    for num in range(x, y+1):
        if num % 2 == 0 and num > largest_even:
            largest_even = num
    return largest_even
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input range",
      "Input Data": "x=1, y=10",
      "Expected Output": "10"
    },
    {
      "Test Title": "Invalid input range",
      "Input Data": "x=-3, y=5",
      "Expected Output": "-1"
    },
    {
      "Test Title": "No even integer in range",
      "Input Data": "x=3, y=7",
      "Expected Output": "-1"
    },
    {
      "Test Title": "Boundary and edge cases",
      "Input Data": "x=0, y=100",
      "Expected Output": "100"
    },
    {
      "Test Title": "Negative input values",
      "Input Data": "x=-10, y=10",
      "Expected Output": "-1"
    },
    {
      "Test Title": "Zero input values",
      "Input Data": "x=0, y=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large input ranges",
      "Input Data": "x=100, y=100000",
      "Expected Output": "100000"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_choose_num(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)

if __name__ == '__main__':
    unittest.main()