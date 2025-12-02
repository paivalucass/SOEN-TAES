def first_odd(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of numbers")
    if not nums:
        return None
    for num in nums:
        if num % 2 != 0:
            return num
    return None

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty List",
      "Input Data": "nums=[]",
      "Expected Output": "None"
    },
    {
      "Test Title": "List with only even numbers",
      "Input Data": "nums=[2,4,6,8]",
      "Expected Output": "None"
    },
    {
      "Test Title": "List with both even and odd numbers",
      "Input Data": "nums=[2,3,4,5,6]",
      "Expected Output": "3"
    },
    {
      "Test Title": "List with negative numbers",
      "Input Data": "nums=[-1,-3,-5,-2,-4]",
      "Expected Output": "-1"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_odd([1,3,5]), 1)

if __name__ == '__main__':
    unittest.main()