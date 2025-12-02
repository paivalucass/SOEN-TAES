def search(lst):
    '''
    This function takes a non-empty list of positive integers as input and returns the greatest integer that is greater than zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, it returns -1.
    '''
    frequency_dict = {}
    for num in lst:
        if num > 0:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
    
    result = -1
    for key, value in frequency_dict.items():
        if key == value and key > result:
            result = key
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()