def tuple_to_int(nums):
    if not isinstance(nums, tuple):
        raise TypeError("Input is not a tuple")
    
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("Tuple contains non-integer values")
    
    if len(nums) == 0:
        raise ValueError("Tuple is empty")
    
    return int(''.join(map(str, nums)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_int((1,2,3)), 123)

if __name__ == '__main__':
    unittest.main()