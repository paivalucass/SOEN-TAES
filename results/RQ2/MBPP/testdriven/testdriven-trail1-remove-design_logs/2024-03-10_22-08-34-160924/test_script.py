def largest_neg(list1):
    '''
    Write a python function to find the largest negative number from the given list.
    assert largest_neg([1,2,3,-4,-6]) == -6
    '''
    largest_negative = None
    for num in list1:
        if num < 0:
            if largest_negative is None or num < largest_negative:
                largest_negative = num
    return largest_negative
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_neg([1,2,3,-4,-6]), -6)

if __name__ == '__main__':
    unittest.main()