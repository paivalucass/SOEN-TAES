def find_first_occurrence(A, x):
    if A is None or len(A) == 0:
        return -1
    left, right = 0, len(A) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] == x:
            result = mid
            right = mid - 1
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Array Test",
      "Input Data": "A=[], x=5",
      "Expected Output": "-1"
    },
    {
      "Test Title": "Single Element Array Test",
      "Input Data": "A=[5], x=5",
      "Expected Output": "0"
    },
    {
      "Test Title": "Multiple Occurrences Test",
      "Input Data": "A=[2, 5, 5, 5, 6, 6, 8, 9, 9, 9], x=5",
      "Expected Output": "1"
    },
    {
      "Test Title": "Null Input Array Test",
      "Input Data": "A=null, x=5",
      "Expected Output": "-1"
    },
    {
      "Test Title": "Element Not Present Test",
      "Input Data": "A=[2, 4, 6, 8], x=5",
      "Expected Output": "-1"
    },
    {
      "Test Title": "Large Input Array Test",
      "Input Data": "A=[1, 2, ..., 9999], x=5",
      "Expected Output": "-1"
    },
    {
      "Test Title": "Maximum Input Value Test",
      "Input Data": "A=[1, 5, 10, 15], x=15",
      "Expected Output": "3"
    },
    {
      "Test Title": "Minimum Input Value Test",
      "Input Data": "A=[1, 5, 10, 15], x=1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Negative Test Case 1",
      "Input Data": "A=[2, 5, 5, 5, 6, 6, 8, 9, 9, 9], x=6",
      "Expected Output": "4"
    },
    {
      "Test Title": "Negative Test Case 2",
      "Input Data": "A=[2, 5, 5, 5, 6, 6, 8, 9, 9, 9], x=9",
      "Expected Output": "7"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()