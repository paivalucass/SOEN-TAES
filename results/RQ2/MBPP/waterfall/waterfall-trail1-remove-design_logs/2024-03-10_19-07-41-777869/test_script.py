def sum_negativenum(nums):
    if not isinstance(nums, list) or len(nums) == 0:
        return 0  

    return sum(n for n in nums if n < 0)  

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Input List",
      "Input Data": "[]",
      "Expected Output": "0"
    },
    {
      "Test Title": "No Negative Numbers in the List",
      "Input Data": "[1, 2, 3, 4, 5]",
      "Expected Output": "0"
    },
    {
      "Test Title": "List with Only One Negative Number",
      "Input Data": "[-5]",
      "Expected Output": "-5"
    },
    {
      "Test Title": "List with Positive and Negative Numbers",
      "Input Data": "[2, 4, -6, -9, 11, -12, 14, -5, 17]",
      "Expected Output": "-32"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]), -32)

if __name__ == '__main__':
    unittest.main()