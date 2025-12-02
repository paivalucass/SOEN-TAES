def even_position(nums):
    if not nums or len(nums) % 2 != 0:
        return False
    
    for i in range(0, len(nums)):
        if i % 2 == 0:
            if not isinstance(nums[i], int) or nums[i] % 2 != 0:
                return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_position([3,2,1]), False)

if __name__ == '__main__':
    unittest.main()