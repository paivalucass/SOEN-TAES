def calculate_square(num):
    return num*num

def square_Sum(n):
    if not isinstance(n, int) or n <= 0:
        return 0
    sum_of_squares = 0
    for i in range(1, 2*n, 2):
        sum_of_squares += calculate_square(i)
    return sum_of_squares

# Test Cases:
{
  "requirement analysis": "test cases for the function to calculate the sum of squares of the first n odd natural numbers",
  "test_cases": [
    {
      "Test Title": "Valid Input Test Case",
      "Input Data": "parameter1=2",
      "Expected Output": "10"
    },
    {
      "Test Title": "Valid Input Test Case - Large Input Value",
      "Input Data": "parameter1=5",
      "Expected Output": "165"
    },
    {
      "Test Title": "Invalid Input Test Case - Non-integer input",
      "Input Data": "parameter1='abc'",
      "Expected Output": "0"
    },
    {
      "Test Title": "Invalid Input Test Case - Non-numeric input",
      "Input Data": "parameter1='xyz'",
      "Expected Output": "0"
    },
    {
      "Test Title": "Boundary Input Test Case - Large Input Value",
      "Input Data": "parameter1=10",
      "Expected Output": "1225"
    },
    {
      "Test Title": "Edge Input Test Case - Large Input Value",
      "Input Data": "parameter1=1",
      "Expected Output": "1"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()