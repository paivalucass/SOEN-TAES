def pair_xor_Sum(arr, n):
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            result += arr[i] ^ arr[j]
    return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Input",
      "Input Data": "arr=[], n=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Input with Single Element",
      "Input Data": "arr=[5], n=1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Input with Multiple Elements",
      "Input Data": "arr=[5, 9, 7, 6], n=4",
      "Expected Output": "47"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pair_xor_Sum([5,9,7,6], 4), 47)

if __name__ == '__main__':
    unittest.main()