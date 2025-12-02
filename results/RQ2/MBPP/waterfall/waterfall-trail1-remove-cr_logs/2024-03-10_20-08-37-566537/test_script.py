def count_Pairs(arr, n):
    if n <= 1:
        return 0

    pair_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                pair_count += 1
    return pair_count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Array Test",
      "Input Data": "arr=[], n=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Single Element Array Test",
      "Input Data": "arr=[1], n=1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Array with Same Elements Test",
      "Input Data": "arr=[1,1,1,1], n=4",
      "Expected Output": "0"
    },
    {
      "Test Title": "Array with Unique Elements Test",
      "Input Data": "arr=[1,2,3,4], n=4",
      "Expected Output": "6"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_count_Pairs(self):
        self.assertEqual(count_Pairs([1,2,1], 3), 2)

if __name__ == '__main__':
    unittest.main()