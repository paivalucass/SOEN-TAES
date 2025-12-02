def get_median(arr1, arr2, n):
    # Validate inputs
    if len(arr1) != n or len(arr2) != n:
        raise ValueError("Input arrays are not of the same size")
    if arr1 != sorted(arr1) or arr2 != sorted(arr2):
        raise ValueError("Input arrays are not sorted in ascending order")
    if not arr1 or not arr2:
        raise ValueError("Input arrays are empty")

    # Identify the middle elements of the two input arrays
    mid1 = arr1[n // 2] if n % 2 != 0 else (arr1[n // 2 - 1] + arr1[n // 2]) / 2
    mid2 = arr2[n // 2] if n % 2 != 0 else (arr2[n // 2 - 1] + arr2[n // 2]) / 2

    # Calculate the median
    if mid1 != mid2:
        return (mid1 + mid2) / 2
    else:
        return mid1

# Test the function
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Validate inputs - Same size",
      "Input Data": "arr1=[1, 12, 15, 26, 38], arr2=[2, 13, 17, 30, 45], n=5",
      "Expected Output": "Pass"
    },
    {
      "Test Title": "Validate inputs - Different size",
      "Input Data": "arr1=[1, 12, 15, 26, 38], arr2=[2, 13, 17, 30], n=5",
      "Expected Output": "Fail"
    },
    {
      "Test Title": "Identify middle elements - Even length",
      "Input Data": "arr=[1, 2, 3, 4], n=4",
      "Expected Output": "Pass"
    },
    {
      "Test Title": "Identify middle elements - Odd length",
      "Input Data": "arr=[1, 2, 3, 4, 5], n=5",
      "Expected Output": "Pass"
    },
    {
      "Test Title": "Calculate median - Different middle elements",
      "Input Data": "arr1=[1, 12, 15, 26, 38], arr2=[2, 13, 17, 30, 45], n=5",
      "Expected Output": "16"
    },
    {
      "Test Title": "Calculate median - Same middle elements",
      "Input Data": "arr1=[1, 12, 15, 26, 38], arr2=[2, 13, 17, 26, 45], n=5",
      "Expected Output": "26"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5), 16.0)

if __name__ == '__main__':
    unittest.main()