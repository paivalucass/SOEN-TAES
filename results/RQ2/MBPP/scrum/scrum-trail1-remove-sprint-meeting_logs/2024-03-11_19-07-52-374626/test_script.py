def check_monthnumber_number(monthnum3):
    if monthnum3 < 1 or monthnum3 > 12:
        raise ValueError("Invalid month number")
    
    # Logic to check if the month contains 30 days
    if monthnum3 in [4, 6, 9, 11]:
        return True
    elif monthnum3 == 2: # Special case for February
        # Logic to check for leap year
        # ... (code for leap year check)
        return "True for leap year and False for non-leap year"
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()