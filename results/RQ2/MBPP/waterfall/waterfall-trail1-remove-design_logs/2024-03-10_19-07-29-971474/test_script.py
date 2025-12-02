def max_occurrences(nums):
    count_dict = {}
    max_count = 0
    max_item = None
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
        if count_dict[num] > max_count:
            max_count = count_dict[num]
            max_item = num
    return max_item

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Find max occurrences in array with negative numbers",
      "Input Data": "nums=[-2, 3, -2, 4, 4, 4, -2, -2]",
      "Expected Output": "-2"
    },
    {
      "Test Title": "Find max occurrences in array with empty input",
      "Input Data": "nums=[]",
      "Expected Output": "null"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)

if __name__ == '__main__':
    unittest.main()