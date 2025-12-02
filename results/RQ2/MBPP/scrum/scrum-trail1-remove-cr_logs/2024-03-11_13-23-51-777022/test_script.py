def check_monthnumb_number(monthnum2):
    thirty_one_days_months = [1, 3, 5, 7, 8, 10, 12]
    
    if monthnum2 in thirty_one_days_months:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumb_number(5), True)

if __name__ == '__main__':
    unittest.main()