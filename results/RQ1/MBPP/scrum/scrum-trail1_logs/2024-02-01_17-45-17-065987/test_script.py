def odd_length_sum(arr):
    total_sum = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n, 2):
            for k in range(i, j+1):
                total_sum += arr[k]
    return total_sum

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Array Test",
      "Input Data": "arr=[]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Array with Negative Numbers Test",
      "Input Data": "arr=[-1,2,-3,4]",
      "Expected Output": "4"
    },
    {
      "Test Title": "Large Array Test",
      "Input Data": "arr=[1,2,3,4,5,6,7,8,9,10]",
      "Expected Output": "105"
    },
    {
      "Test Title": "Edge Case - Array with Negative Numbers Test",
      "Input Data": "arr=[-5]",
      "Expected Output": "-5"
    },
    {
      "Test Title": "Edge Case - Array with one element Test",
      "Input Data": "arr=[5]",
      "Expected Output": "5"
    },
    {
      "Test Title": "Edge Case - Array with duplicate elements Test",
      "Input Data": "arr=[2,2,2]",
      "Expected Output": "10"
    },
    {
      "Test Title": "Boundary Case - Smallest possible input array Test",
      "Input Data": "arr=[1]",
      "Expected Output": "1"
    },
    {
      "Test Title": "Boundary Case - Largest possible input array Test",
      "Input Data": "arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]",
      "Expected Output": "484"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_length_sum([1,2,4]), 14)

if __name__ == '__main__':
    unittest.main()