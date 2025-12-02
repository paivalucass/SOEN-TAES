def is_majority(arr, n, x):
    count = arr.count(x)
    return count > n/2

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Majority Element",
      "Input Data": "arr=[1, 2, 3, 3, 3, 3, 10], n=7, x=3",
      "Expected Output": "True"
    },
    {
      "Test Title": "Invalid Majority Element",
      "Input Data": "arr=[1, 2, 3, 3, 10], n=5, x=3",
      "Expected Output": "False"
    },
    {
      "Test Title": "Empty Array",
      "Input Data": "arr=[], n=0, x=3",
      "Expected Output": "False"
    },
    {
      "Test Title": "Single Element Array",
      "Input Data": "arr=[3], n=1, x=3",
      "Expected Output": "True"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3), True)

if __name__ == '__main__':
    unittest.main()