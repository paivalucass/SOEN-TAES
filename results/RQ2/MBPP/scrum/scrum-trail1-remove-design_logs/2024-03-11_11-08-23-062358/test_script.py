def sum_Of_Subarray_Prod(arr):
    result = 0
    mod = 10**9 + 7
    n = len(arr)
    for i in range(n):
        result = (result + arr[i] * (i + 1) * (n - i)) % mod
    return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty List Test",
      "Input Data": "arr=[]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Single Element Test",
      "Input Data": "arr=[5]",
      "Expected Output": "5"
    },
    {
      "Test Title": "Positive Numbers Test",
      "Input Data": "arr=[1,2,3]",
      "Expected Output": "20"
    },
    {
      "Test Title": "Negative Numbers Test",
      "Input Data": "arr=[-1,-2,-3]",
      "Expected Output": "6"
    },
    {
      "Test Title": "Large List Test",
      "Input Data": "arr=[1,2,3,4,5]",
      "Expected Output": "384"
    },
    {
      "Test Title": "Array with all zeros",
      "Input Data": "arr=[0,0,0]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Mix of positive and negative numbers",
      "Input Data": "arr=[-1,2,-3]",
      "Expected Output": "-2"
    },
    {
      "Test Title": "Minimum and Maximum Values Test",
      "Input Data": "arr=[-1000,1000]",
      "Expected Output": "-1000000"
    },
    {
      "Test Title": "Large Input Data Test",
      "Input Data": "arr=[1,2,3,4,5,6,7,8,9,10]",
      "Expected Output": "3628800"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_sum_Of_Subarray_Prod(self):
        self.assertEqual(sum_Of_Subarray_Prod([1,2,3]), 20)

if __name__ == '__main__':
    unittest.main()