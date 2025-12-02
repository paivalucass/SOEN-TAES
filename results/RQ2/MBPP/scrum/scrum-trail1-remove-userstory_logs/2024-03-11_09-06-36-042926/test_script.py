def get_Inv_Count(arr):
    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Array",
      "Input Data": "arr=[]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Array with One Element",
      "Input Data": "arr=[5]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Array with Multiple Elements",
      "Input Data": "arr=[1, 20, 6, 4, 5]",
      "Expected Output": "5"
    },
    {
      "Test Title": "Negative Numbers",
      "Input Data": "arr=[-3, -5, -2, -8]",
      "Expected Output": "6"
    },
    {
      "Test Title": "Large Numbers",
      "Input Data": "arr=[1000, 500, 2000, 1500]",
      "Expected Output": "6"
    },
    {
      "Test Title": "Array with Duplicate Elements",
      "Input Data": "arr=[2, 3, 2, 3, 4]",
      "Expected Output": "2"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Inv_Count([1,20,6,4,5]), 5)

if __name__ == '__main__':
    unittest.main()