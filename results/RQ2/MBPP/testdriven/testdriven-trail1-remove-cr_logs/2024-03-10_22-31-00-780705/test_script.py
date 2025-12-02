def tuple_to_int(nums):
    """
    Function to convert a given tuple of positive integers into a single integer.
    
    Args:
    nums (tuple): Tuple of positive integers
    
    Returns:
    int: Single integer formed by concatenating the integers in the tuple
    """
    if not nums:
        return "Error: Empty input tuple"
    
    for num in nums:
        if not isinstance(num, int) or num <= 0:
            return "Error: Negative number in input tuple" if num <= 0 else "Error: Non-numeric inputs in input tuple"
    
    result = int(''.join(map(str, nums)))
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_int((1,2,3)), 123)

if __name__ == '__main__':
    unittest.main()