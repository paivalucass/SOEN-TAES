def check_monthnumb_number(monthnum2, leapyear=False):
    days_in_month = {
        1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
        4: 30, 6: 30, 9: 30, 11: 30,
        2: 29 if leapyear else 28
    }

    if monthnum2 in days_in_month and monthnum2 > 0:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumb_number(5), True)

if __name__ == '__main__':
    unittest.main()