def zero_count(nums):
    zero_count = 0
    non_zero_count = 0
    
    if not isinstance(nums, list):
        return "Error message"
    
    if len(nums) == 0:
        return "Error message"
    
    for num in nums:
        if not isinstance(num, int):
            return "Error message"
        if num == 0:
            zero_count += 1
        else:
            non_zero_count += 1
            
    if non_zero_count == 0:
        return "Ratio of zeroes to non-zeroes: Infinity"
    
    return round(zero_count / non_zero_count, 6) # Rounded to 6 decimal places

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty array input",
      "Input Data": "parameter1=[]",
      "Expected Output": "Error message"
    },
    {
      "Test Title": "Array with only zeroes input",
      "Input Data": "parameter1=[0, 0, 0]",
      "Expected Output": "Ratio of zeroes to non-zeroes: Infinity"
    },
    {
      "Test Title": "Large input array",
      "Input Data": "parameter1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]",
      "Expected Output": "Ratio of zeroes to non-zeroes: 0"
    },
    {
      "Test Title": "Negative input values",
      "Input Data": "parameter1=[-1, -2, -3]",
      "Expected Output": "Ratio of zeroes to non-zeroes: 0"
    },
    {
      "Test Title": "Non-integer input values",
      "Input Data": "parameter1=[1.5, 2.5, 3.5]",
      "Expected Output": "Error message"
    },
    {
      "Test Title": "Large input array with mix of zeroes and non-zeroes",
      "Input Data": "parameter1=[0, 1, 0, 2, 0, 3, 4, 5, 6, 0, 7, 8, 9]",
      "Expected Output": "Ratio of zeroes to non-zeroes: 0.363636"
    },
    {
      "Test Title": "Null input",
      "Input Data": "parameter1=null",
      "Expected Output": "Error message"
    },
    {
      "Test Title": "Non-array input",
      "Input Data": "parameter1='123'",
      "Expected Output": "Error message"
    },
    {
      "Test Title": "Input arrays with a mix of different data types",
      "Input Data": "parameter1=[1, 'abc', true]",
      "Expected Output": "Error message"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_zero_count(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, places=6)

if __name__ == '__main__':
    unittest.main()