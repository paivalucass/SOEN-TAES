def test_duplicate(arraynums):
    nums = arraynums.copy()
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_duplicate([1,2,3,4,5]), False)

if __name__ == '__main__':
    unittest.main()