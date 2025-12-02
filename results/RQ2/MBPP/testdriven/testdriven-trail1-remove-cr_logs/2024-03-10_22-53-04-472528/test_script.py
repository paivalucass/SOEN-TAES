def odd_position(nums):
    if not all(isinstance(x, int) for x in nums):
        return "Input must be a list of numbers"
    
    result = True
    for i in range(1, len(nums), 2):
        if nums[i] % 2 == 0:
            result = False
            break
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_position([2,1,4,3,6,7,6,3]), True)

if __name__ == '__main__':
    unittest.main()