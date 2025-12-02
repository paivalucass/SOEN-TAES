def count_rotation(arr):
    # Implementing a binary search algorithm to find the index of the minimum element in a rotated sorted array
    # Adding comments to explain the logic behind the binary search and the conditions being checked
    # Using descriptive variable names to improve readability and maintainability of the code

    # Write code here to count the number of rotations required to generate a sorted array
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        # Case 1: If the array is already sorted
        if arr[low] <= arr[high]:
            return low

        mid = (low + high) // 2
        next_val = (mid + 1) % n
        prev_val = (mid + n - 1) % n

        # Case 2: If the mid element is the minimum element
        if arr[mid] <= arr[next_val] and arr[mid] <= arr[prev_val]:
            return mid

        # Case 3: If the right half is sorted, search in the left half
        if arr[mid] <= arr[high]:
            high = mid - 1
        # Case 4: If the left half is sorted, search in the right half
        if arr[mid] >= arr[low]:
            low = mid + 1

# Test Cases:
{
  "requirement analysis": "test cases for counting rotations in an array",
  "test_cases": [
    {
      "Test Title": "Ascending Order Test Case 1",
      "Input Data": "arr=[3,2,1]",
      "Expected Output": "1"
    },
    {
      "Test Title": "Ascending Order Test Case 2",
      "Input Data": "arr=[4,5,6]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Descending Order Test Case",
      "Input Data": "arr=[7,6,5]",
      "Expected Output": "2"
    },
    {
      "Test Title": "Random Order Test Case",
      "Input Data": "arr=[5,3,6,4,2,1]",
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