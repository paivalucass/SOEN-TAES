def even_position(nums):
    for i in range(len(nums)):
        if i % 2 == 0 and nums[i] % 2 != 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_position([3, 2, 1]), False)

if __name__ == '__main__':
    unittest.main()