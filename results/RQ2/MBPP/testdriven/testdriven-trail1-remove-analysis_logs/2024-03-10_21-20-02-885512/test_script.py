def largest_neg(list1):
    '''
    Write a python function to find the largest negative number from the given list.
    assert largest_neg([1,2,3,-4,-6]) == -6
    '''

    neg_numbers = [num for num in list1 if num < 0]
    
    if not neg_numbers:
        return None
    else:
        return min(neg_numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_neg([1,2,3,-4,-6]), -6)

if __name__ == '__main__':
    unittest.main()