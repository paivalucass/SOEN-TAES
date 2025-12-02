def check_monthnumber_number(monthnum):
    thirty_days_months = [4, 6, 9, 11]
    if monthnum < 1 or monthnum > 12:
        return False
    if monthnum in thirty_days_months:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()