def largest_neg(list1):
    if not isinstance(list1, list) or not all(isinstance(x, (int, float)) for x in list1):
        return "Input is not a list of numbers"

    neg_nums = [num for num in list1 if num < 0]
    if not neg_nums:
        return "No negative numbers in the input list"

    return min(neg_nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_neg([1,2,3,-4,-6]), -6)

if __name__ == '__main__':
    unittest.main()