def even_position(nums):
    if not isinstance(nums, list):
        raise TypeError("Input is not a list")
    for i in range(len(nums)):
        if i % 2 == 0:
            if not isinstance(nums[i], (int, float)):
                raise ValueError("Elements in the list are not numbers")
            if nums[i] % 2 != 0:
                return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_position([3,2,1]), False)

if __name__ == '__main__':
    unittest.main()