def largest_neg(list1):
    if not isinstance(list1, list):
        raise ValueError("Input must be a list")
    
    neg_nums = [num for num in list1 if num < 0]
    
    if len(neg_nums) == 0:
        return None
    else:
        return min(neg_nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_neg([1,2,3,-4,-6]), -6)

if __name__ == '__main__':
    unittest.main()