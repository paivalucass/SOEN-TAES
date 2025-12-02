def count_rotation(arr):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        next_val = (mid + 1) % n
        prev_val = (mid + n - 1) % n

        if arr[mid] <= arr[next_val] and arr[mid] <= arr[prev_val]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1
    
    return 0  # Default return if array is already sorted

# Test Cases:
{
  "test_cases": [
    {
      "TestTitle": "Input array of different lengths",
      "InputData": "parameter1=[1,2,3,4,5], parameter2=[5,4,3,2,1]",
      "ExpectedOutput": "2"
    },
    {
      "TestTitle": "Sorted array input",
      "InputData": "parameter1=[1,2,3,4,5], parameter2=[1,2,3,4,5]",
      "ExpectedOutput": "0"
    },
    {
      "TestTitle": "Unsorted array input",
      "InputData": "parameter1=[3,1,2,5,4], parameter2=[4,5,2,1,3]",
      "ExpectedOutput": "3"
    },
    {
      "TestTitle": "Edge case scenario",
      "InputData": "parameter1=[1], parameter2=[1]",
      "ExpectedOutput": "0"
    },
    {
      "TestTitle": "Empty array input",
      "InputData": "parameter1=[], parameter2=[]",
      "ExpectedOutput": "0"
    },
    {
      "TestTitle": "Large array input",
      "InputData": "parameter1=[1,2,3,4,5,6,7,8,9,10], parameter2=[10,9,8,7,6,5,4,3,2,1]",
      "ExpectedOutput": "9"
    },
    {
      "TestTitle": "Array with duplicate elements input",
      "InputData": "parameter1=[1,2,3,3,4,5], parameter2=[5,4,3,2,2,1]",
      "ExpectedOutput": "5"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()