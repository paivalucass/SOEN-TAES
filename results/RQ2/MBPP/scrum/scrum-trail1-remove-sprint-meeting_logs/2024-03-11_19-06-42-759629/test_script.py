def check_min_heap_helper(arr, i):
    if not arr:
        return False

    if not all(isinstance(x, int) for x in arr):
        return False

    def is_min_heap(arr, i, n):
        if i >= n:
            return True
        left = 2 * i + 1
        right = 2 * i + 2
        if (left < n and arr[left] < arr[i]) or (right < n and arr[right] < arr[i]):
            return False
        return is_min_heap(arr, left, n) and is_min_heap(arr, right, n)

    n = len(arr)
    return is_min_heap(arr, i, n)

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Min Heap Array",
      "Input Data": "arr=[1,2,3,4,5,6], i=0",
      "Expected Output": "True"
    },
    {
      "Test Title": "Invalid Min Heap Array",
      "Input Data": "arr=[5,4,3,2,1], i=0",
      "Expected Output": "False"
    },
    {
      "Test Title": "Empty Array",
      "Input Data": "arr=[], i=0",
      "Expected Output": "True"
    },
    {
      "Test Title": "Array with Duplicate Elements",
      "Input Data": "arr=[1,1,1,1,1], i=0",
      "Expected Output": "True"
    },
    {
      "Test Title": "Array with Negative Numbers",
      "Input Data": "arr=[-1,-2,-3,-4,-5,-6], i=0",
      "Expected Output": "True"
    },
    {
      "Test Title": "Array with Large Values",
      "Input Data": "arr=[1000,2000,3000,4000,5000,6000], i=0",
      "Expected Output": "True"
    },
    {
      "Test Title": "Array with Different 'i' Values",
      "Input Data": "arr=[1,2,3,4,5,6], i=2",
      "Expected Output": "True"
    },
    {
      "Test Title": "Array with Mixed Data Types",
      "Input Data": "arr=[1,'2',3.0,'4',5.5,6], i=0",
      "Expected Output": "True"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_min_heap_helper([1, 2, 3, 4, 5, 6], 0), True)

if __name__ == '__main__':
    unittest.main()