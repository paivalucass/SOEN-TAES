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
      "Test Title": "Empty Input List",
      "Input Data": "arr=[], n=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "List with a Single Element",
      "Input Data": "arr=[5], n=1",
      "Expected Output": "0"
    },
    {
      "Test Title": "List with Multiple Elements",
      "Input Data": "arr=[5,9,7,6], n=4",
      "Expected Output": "47"
    },
    {
      "Test Title": "Negative Numbers",
      "Input Data": "arr=[-5,-9,7,6], n=4",
      "Expected Output": "108"
    },
    {
      "Test Title": "Large Input List",
      "Input Data": "arr=[1,2,3,...,1000], n=1000",
      "Expected Output": "some_expected_output"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pair_xor_Sum([5,9,7,6], 4), 47)

if __name__ == '__main__':
    unittest.main()