def pancake_sort(nums):
    def partition(arr, low, high):
        i = (low-1)         
        pivot = arr[high]     
     
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
     
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)
     
    def quickSort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            quickSort(arr, low, pi-1)
            quickSort(arr, pi+1, high)
    
    quickSort(nums, 0, len(nums)-1)
    return nums

# Test Cases:
{
  "requirement_analysis": "Write test cases for pancake_sort function",
  "test_cases": [
    {
      "Test Title": "Sort in ascending order",
      "Input Data": "nums=[15, 79, 25, 38, 69]",
      "Expected Output": "[15, 25, 38, 69, 79]"
    },
    {
      "Test Title": "Sort in descending order",
      "Input Data": "nums=[69, 38, 25, 79, 15]",
      "Expected Output": "[15, 25, 38, 69, 79]"
    },
    {
      "Test Title": "Sort a single element",
      "Input Data": "nums=[1]",
      "Expected Output": "[1]"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()