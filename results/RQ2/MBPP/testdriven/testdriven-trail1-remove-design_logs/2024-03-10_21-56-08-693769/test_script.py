def pos_count(nums):
    count = len([num for num in nums if num > 0])
    return count

# Test Cases:
assert pos_count([]) == 0
assert pos_count([-1, -2, -3]) == 0
assert pos_count([1, 2, 3]) == 3
assert pos_count([1, -2, 3, -4]) == 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pos_count([1,-2,3,-4]), 2)

if __name__ == '__main__':
    unittest.main()