def count_rotation(arr):
    rotations = 0
    if len(arr) == 0:
        return rotations
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        next_index = (mid + 1) % len(arr)
        prev_index = (mid + len(arr) - 1) % len(arr)
        if arr[mid] <= arr[next_index] and arr[mid] <= arr[prev_index]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1
    return rotations

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test 1",
      "Input Data": "arr=[3,2,1]",
      "Expected Output": "1"
    },
    {
      "Test Title": "Test 2",
      "Input Data": "arr=[]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Test 3",
      "Input Data": "arr=[1,2,3,4,5,6,7,8,9,10]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Test 4",
      "Input Data": "arr=[3,3,3,3,3]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Test 5",
      "Input Data": "arr=[5,4,3,2,1]",
      "Expected Output": "4"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()