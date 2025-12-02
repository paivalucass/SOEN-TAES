def check_month_number(monthnum):
    '''Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.'''
    if monthnum in [4, 6, 9, 11]:
        return True
    else:
        return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()