def pancake_sort(nums):
    if not nums:
        raise ValueError("Input list is empty")
    
    if not isinstance(nums, list):
        raise TypeError("Input is not a list of elements")
    
    sorted_nums = sorted(nums)
    
    return sorted_nums
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()