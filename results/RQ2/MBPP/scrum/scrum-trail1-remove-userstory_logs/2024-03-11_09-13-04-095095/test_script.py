def check_monthnumb_number(monthnum):
    '''Write a function to check whether the given month number contains 31 days or not.'''
    if monthnum in [1, 3, 5, 7, 8, 10, 12]:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumb_number(5), True)

if __name__ == '__main__':
    unittest.main()