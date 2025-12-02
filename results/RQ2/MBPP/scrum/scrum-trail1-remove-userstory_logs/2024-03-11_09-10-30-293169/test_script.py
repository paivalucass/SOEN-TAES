def filter_oddnumbers(nums):
    if not nums or not all(isinstance(x, int) for x in nums):
        return "Input list is either empty or contains non-integer elements"
    return list(filter(lambda x: x % 2 != 0, nums))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()