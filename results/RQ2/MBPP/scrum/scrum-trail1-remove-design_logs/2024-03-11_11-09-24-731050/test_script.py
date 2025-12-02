def find_Index(n):
    triangular_number = 1
    index = 1
    while len(str(triangular_number)) < n:
        index += 1
        triangular_number += index
    return index

# Test the function with edge cases such as n = 1, n = 2, and n = 3 to ensure it returns the correct index.
# Also, consider adding boundary value testing to check for any potential issues with large input values.
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test for n=2",
      "Input Data": "n=2",
      "Expected Output": "4"
    },
    {
      "Test Title": "Test for n=3",
      "Input Data": "n=3",
      "Expected Output": "10"
    },
    {
      "Test Title": "Test for n=4",
      "Input Data": "n=4",
      "Expected Output": "20"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Index(2), 4)

if __name__ == '__main__':
    unittest.main()