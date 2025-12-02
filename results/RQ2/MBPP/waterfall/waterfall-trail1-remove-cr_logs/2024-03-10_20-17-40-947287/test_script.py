def get_pairs_count(arr, sum):
    if len(arr) == 0:
        return 0

    pair_count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                pair_count += 1
    return pair_count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Input List",
      "Input Data": "arr=[], sum=10",
      "Expected Output": "0"
    },
    {
      "Test Title": "Negative Numbers in Input List",
      "Input Data": "arr=[-1, 2, 3, -4, 5], sum=0",
      "Expected Output": "2"
    },
    {
      "Test Title": "Negative Numbers in Input List",
      "Input Data": "arr=[-1, -1, -1, -1], sum=-2",
      "Expected Output": "6"
    },
    {
      "Test Title": "Large Input List",
      "Input Data": "arr=[1000000, 2000000, 3000000], sum=4000000",
      "Expected Output": "0"
    },
    {
      "Test Title": "Input List with One Element",
      "Input Data": "arr=[5], sum=5",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large Numbers in Input List",
      "Input Data": "arr=[999999999, 999999999], sum=1999999998",
      "Expected Output": "1"
    },
    {
      "Test Title": "Performance and Scalability Testing",
      "Input Data": "arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], sum=20",
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