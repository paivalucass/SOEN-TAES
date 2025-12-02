def neg_nos(list1):
    '''
    Write a python function to return the negative numbers in a list.
    assert neg_nos([-1,4,5,-6]) == [-1,-6]
    '''
    if not isinstance(list1, list):
        raise TypeError("Input must be a list")
    
    negative_numbers = [num for num in list1 if num < 0]
    return negative_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(neg_nos([-1,4,5,-6]), [-1,-6])

if __name__ == '__main__':
    unittest.main()