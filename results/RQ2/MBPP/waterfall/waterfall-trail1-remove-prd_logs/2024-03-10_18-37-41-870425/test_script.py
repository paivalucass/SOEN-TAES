def find_Average_Of_Cube(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input: n should be a positive integer"

    sum_cubes = sum([i ** 3 for i in range(1, n+1)])
    average_cubes = sum_cubes / n
    return round(average_cubes, 1) # rounding to 1 decimal place

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input Test",
      "Input Data": "n=2",
      "Expected Output": "4.5"
    },
    {
      "Test Title": "Edge Case Test (n=0)",
      "Input Data": "n=0",
      "Expected Output": "Error message indicating invalid input"
    },
    {
      "Test Title": "Edge Case Test (n=1)",
      "Input Data": "n=1",
      "Expected Output": "1.0"
    },
    {
      "Test Title": "Boundary Test (n=10)",
      "Input Data": "n=10",
      "Expected Output": "302.5"
    },
    {
      "Test Title": "Negative Input Test (n=-3)",
      "Input Data": "n=-3",
      "Expected Output": "Error message indicating invalid input"
    },
    {
      "Test Title": "Non-integer Input Test (n=3.5)",
      "Input Data": "n=3.5",
      "Expected Output": "Error message indicating invalid input"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()