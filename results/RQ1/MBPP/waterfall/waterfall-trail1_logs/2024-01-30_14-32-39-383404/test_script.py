def check_monthnumb_number(monthnum2):
    if not isinstance(monthnum2, int):
        raise ValueError("Invalid input: month number must be an integer.")
    
    if monthnum2 <= 0 or monthnum2 > 12:
        raise ValueError("Invalid input: month number must be between 1 and 12.")
    
    # List of months with 31 days
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]

    if monthnum2 in months_with_31_days:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumb_number(5), True)

if __name__ == '__main__':
    unittest.main()