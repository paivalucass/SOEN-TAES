def unique_Element(arr):
    '''Write a python function to check whether a list of numbers contains only one distinct element or not.'''
    if len(set(arr)) <= 1:
        return True
    else:
        return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_Element([1,1,1]), True)

if __name__ == '__main__':
    unittest.main()