def smallest_change(arr):
    if arr == []:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        changes = 0
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                changes += 1
            left += 1
            right -= 1
        return changes

# Test Cases:
{
  "requirement analysis": "analysis",
  "test_cases": [
    {
      "Test Title": "non_empty_array_with_positive_integers",
      "Input Data": "arr=[1,2,3,5,4,7,9,6]",
      "Expected Output": "4"
    },
    {
      "Test Title": "non_empty_array_with_mixed_integers",
      "Input Data": "arr=[1, 2, 3, 4, 3, 2, 2]",
      "Expected Output": "1"
    },
    {
      "Test Title": "non_empty_palindromic_array",
      "Input Data": "arr=[1, 2, 3, 2, 1]",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_smallest_change(self):
        self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

if __name__ == '__main__':
    unittest.main()