def check_monthnumber_number(monthnum3):
    '''Function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.'''
    if monthnum3 < 1 or monthnum3 > 12:
        raise ValueError("Invalid input: Month number should be within the range of 1 to 12.")
    if monthnum3 in [4, 6, 9, 11]:
        return True
    else:
        return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()