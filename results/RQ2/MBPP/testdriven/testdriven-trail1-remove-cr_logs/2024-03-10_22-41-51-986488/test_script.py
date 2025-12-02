def largest_neg(list1):
    try:
        if not isinstance(list1, list):
            raise TypeError("Input is not a list")
        
        if len(list1) == 0:
            raise ValueError("Input list is empty")
        
        largest_neg_num = None
        for num in list1:
            if num < 0:
                if largest_neg_num is None or num < largest_neg_num:
                    largest_neg_num = num
        
        if largest_neg_num is None:
            raise ValueError("No negative numbers found in the input list")
        
        return largest_neg_num
        
    except TypeError as e:
        return e
    except ValueError as e:
        return e

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_neg([1,2,3,-4,-6]), -6)

if __name__ == '__main__':
    unittest.main()