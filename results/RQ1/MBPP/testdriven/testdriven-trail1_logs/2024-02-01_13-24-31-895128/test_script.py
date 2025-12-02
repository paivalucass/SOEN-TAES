def check_month_number(month_number):
    '''Function to check whether the given month number contains 30 days or not. Months are given as numbers from 1 to 12.'''
    if month_number < 1 or month_number > 12:
        return False
    elif month_number in [4, 6, 9, 11]:
        return True
    else:
        return False

# Testing the function with an assertion
assert check_month_number(6) == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()