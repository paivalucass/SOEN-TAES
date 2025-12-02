def even_position(nums):
    try:
        if not isinstance(nums, list):
            raise ValueError("Input is not a list")
        for num in nums:
            if not isinstance(num, int):
                raise ValueError("List contains non-integer values")
        
        for i in range(0, len(nums), 2):
            if nums[i] % 2 != 0:
                return False
        return True
        
    except (ValueError, IndexError):
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_position([3,2,1]), False)

if __name__ == '__main__':
    unittest.main()