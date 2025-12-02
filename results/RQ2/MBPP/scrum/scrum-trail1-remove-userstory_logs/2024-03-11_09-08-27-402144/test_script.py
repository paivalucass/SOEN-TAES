def median_numbers(a, b, c):
    nums = [a, b, c]
    nums.sort()
    return nums[1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_numbers(25, 55, 65), 55.0)

if __name__ == '__main__':
    unittest.main()