def get_pairs_count(arr, target_sum):
    freq_map = {}
    pairs = 0
    for num in arr:
        if target_sum - num in freq_map:
            pairs += freq_map[target_sum - num]
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    return pairs

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input with multiple pairs",
      "Input Data": "arr=[1,1,1,1], sum=2",
      "Expected Output": "6"
    },
    {
      "Test Title": "Valid input with no pairs",
      "Input Data": "arr=[1,2,3,4,5], sum=10",
      "Expected Output": "0"
    },
    {
      "Test Title": "Input with negative numbers",
      "Input Data": "arr=[-1,2,-3,4,5], sum=1",
      "Expected Output": "2"
    },
    {
      "Test Title": "Valid input with empty array",
      "Input Data": "arr=[], sum=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Valid input with only one element in the array",
      "Input Data": "arr=[5], sum=5",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_get_pairs_count(self):
        self.assertEqual(get_pairs_count([1, 1, 1, 1], 2), 6)

if __name__ == '__main__':
    unittest.main()