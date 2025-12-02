def find_kth(arr1, arr2, k):
    merged_array = merge_sorted_arrays(arr1, arr2)
    return merged_array[k-1]

def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    merged_array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    merged_array += arr1[i:]
    merged_array += arr2[j:]
    return merged_array

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input",
      "Input Data": "arr1=[2, 3, 6, 7, 9], arr2=[1, 4, 8, 10], k=5",
      "Expected Output": 6
    },
    {
      "Test Title": "Different input values",
      "Input Data": "arr1=[1, 3, 5, 7], arr2=[2, 4, 6, 8], k=3",
      "Expected Output": 3
    },
    {
      "Test Title": "Equal input values",
      "Input Data": "arr1=[1, 2, 3], arr2=[4, 5, 6], k=4",
      "Expected Output": 4
    },
    {
      "Test Title": "Empty array",
      "Input Data": "arr1=[], arr2=[1, 2, 3], k=2",
      "Expected Output": 2
    },
    {
      "Test Title": "Negative input values",
      "Input Data": "arr1=[-3, -2, 0, 1], arr2=[-5, -4, -1], k=3",
      "Expected Output": -1
    },
    {
      "Test Title": "Large input arrays",
      "Input Data": "arr1=[1, 2, 3, ..., 1000], arr2=[1001, 1002, 1003, ..., 2000], k=1500",
      "Expected Output": 1500
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()