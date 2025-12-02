def first_odd(nums):
    if not nums or not all(isinstance(x, (int, float)) for x in nums):
        return None
    for num in nums:
        if num % 2 != 0:
            return num
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_odd([1,3,5]), 1)

if __name__ == '__main__':
    unittest.main()