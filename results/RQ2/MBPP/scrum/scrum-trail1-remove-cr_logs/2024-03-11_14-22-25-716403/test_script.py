def count_rotation(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        start = 0
        end = len(arr) - 1
        while start <= end:
            if arr[start] <= arr[end]:
                return start
            mid = (start + end) // 2
            next_mid = (mid + 1) % len(arr)
            prev_mid = (mid - 1 + len(arr)) % len(arr)
            if arr[mid] <= arr[next_mid] and arr[mid] <= arr[prev_mid]:
                return mid
            elif arr[mid] <= arr[end]:
                end = mid - 1
            elif arr[mid] >= arr[start]:
                start = mid + 1
        return -1  # in case of no rotations

# Test Cases:
{
  "requirement_analysis":"count the number of rotations required to generate a sorted array",
  "test_cases":[
    {
      "Test Title":"Valid input array",
      "Input Data":"arr=[3,2,1]",
      "Expected Output":"1"
    },
    {
      "Test Title":"Empty input array",
      "Input Data":"arr=[]",
      "Expected Output":"0"
    },
    {
      "Test Title":"Input array with single element",
      "Input Data":"arr=[5]",
      "Expected Output":"0"
    },
    {
      "Test Title":"Input array with multiple elements",
      "Input Data":"arr=[1,2,3,4,5]",
      "Expected Output":"0"
    },
    {
      "Test Title":"Input array with only two elements",
      "Input Data":"arr=[1,2]",
      "Expected Output":"0"
    },
    {
      "Test Title":"Input array with duplicate elements",
      "Input Data":"arr=[2,2,3,4,5]",
      "Expected Output":"2"
    },
    {
      "Test Title":"Input array with already sorted elements",
      "Input Data":"arr=[1,2,3,4,5]",
      "Expected Output":"0"
    },
    {
      "Test Title":"Boundary test - maximum possible elements",
      "Input Data":"arr=[1,2,3,...,1000]",
      "Expected Output":"0"
    },
    {
      "Test Title":"Boundary test - minimum possible elements",
      "Input Data":"arr=[1]",
      "Expected Output":"0"
    },
    {
      "Test Title":"Negative test case - input array not in descending order",
      "Input Data":"arr=[1,2,1,4,5]",
      "Expected Output":"2"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()