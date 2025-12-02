def largest_neg(list1):
    if not isinstance(list1, list) or not all(isinstance(x, int) for x in list1):
        return "Input should be a list of integers"
    
    if len(list1) == 0:
        return "Input list is empty"
    
    neg_nums = [x for x in list1 if x < 0]
    if not neg_nums:
        return "There are no negative numbers in the list"
    return min(neg_nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_neg([1,2,3,-4,-6]), -6)

if __name__ == '__main__':
    unittest.main()