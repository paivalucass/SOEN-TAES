def check_monthnumber_number(monthnum3):
    THIRTY_DAYS_MONTHS = [4, 6, 9, 11]
    if monthnum3 in THIRTY_DAYS_MONTHS:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()