def min_of_three(a, b, c):
    # Input validation
    if not all(isinstance(num, (int, float)) for num in [a, b, c]):
        raise ValueError("Input values must be numbers")  # Input validation improved by using isinstance()

    # Logic for finding the minimum of three numbers
    # Compare the three numbers
    min_num = min(a, b, c)  # Finding the minimum of three numbers
    # Return the minimum of the three numbers
    return min_num  # Returning the minimum of the three numbers

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input - Test case 1",
      "Input Data": "a=1,b=2,c=3",
      "Expected Output": 1
    },
    {
      "Test Title": "Valid input - Test case 2",
      "Input Data": "a=-1,b=-2,c=-3",
      "Expected Output": -3
    },
    {
      "Test Title": "Invalid input - Test case 1",
      "Input Data": "a=1,b=2,c='a'",
      "Expected Output": "ValueError"
    },
    {
      "Test Title": "Edge case - Test case 1",
      "Input Data": "a=0,b=0,c=0",
      "Expected Output": 0
    },
    {
      "Test Title": "Boundary condition - Test case 1",
      "Input Data": "a=-1000000,b=0,c=1000000",
      "Expected Output": -1000000
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_of_three(10, 20, 0), 0)

if __name__ == '__main__':
    unittest.main()