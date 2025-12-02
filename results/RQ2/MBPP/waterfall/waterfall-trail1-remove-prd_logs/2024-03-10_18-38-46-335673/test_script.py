def largest_neg(list1):
    if not all(isinstance(x, (int, float)) for x in list1):
        raise ValueError("Input list should contain only numbers")

    neg_nums = [x for x in list1 if x < 0]
    if len(neg_nums) == 0:
        raise ValueError("Input list should contain at least one negative number")

    return min(neg_nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_neg([1,2,3,-4,-6]), -6)

if __name__ == '__main__':
    unittest.main()