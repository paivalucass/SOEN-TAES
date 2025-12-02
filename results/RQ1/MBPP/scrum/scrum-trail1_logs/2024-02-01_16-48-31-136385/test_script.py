def get_pairs_count(arr, sum):
    pairs_count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                pairs_count += 1
    return pairs_count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty List",
      "Input Data": "arr=[], sum=5",
      "Expected Output": "0"
    },
    {
      "Test Title": "Negative Numbers",
      "Input Data": "arr=[-1, 2, 3, 4, -2, 1], sum=2",
      "Expected Output": "4"
    },
    {
      "Test Title": "Sum of 0",
      "Input Data": "arr=[-1, 2, 3, 4, -2, 1], sum=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "One Element List",
      "Input Data": "arr=[5], sum=5",
      "Expected Output": "0"
    },
    {
      "Test Title": "Empty List with Sum 0",
      "Input Data": "arr=[], sum=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large Input Data",
      "Input Data": "arr=[1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000], sum=2000000000",
      "Expected Output": "6"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_pairs_count([1,1,1,1], 2), 6)

if __name__ == '__main__':
    unittest.main()