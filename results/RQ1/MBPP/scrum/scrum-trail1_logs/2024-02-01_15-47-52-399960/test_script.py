def cube_nums(nums):
    """
    Function to find cubes of individual elements in a list.
    
    Args:
    nums (list): List of numbers
    
    Returns:
    list: New list with cubes of each number
    """
    # Handle edge cases
    if not nums:
        return []
    
    try:
        # Calculate cubes using list comprehension
        return [num ** 3 for num in nums]
    except TypeError:
        # Handle non-numeric elements in the list
        raise ValueError("Input list contains non-numeric elements")

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty List",
      "Input Data": "nums=[]",
      "Expected Output": "[]"
    },
    {
      "Test Title": "Single Element List",
      "Input Data": "nums=[1]",
      "Expected Output": "[1]"
    },
    {
      "Test Title": "Large Number of Elements",
      "Input Data": "nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
      "Expected Output": "[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]"
    },
    {
      "Test Title": "Passing a String",
      "Input Data": "nums='invalid_input'",
      "Expected Output": "Error: Invalid input, input must be a list"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])

if __name__ == '__main__':
    unittest.main()