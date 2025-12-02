import re

def valid_date(date):
    date_format = r"^\d{2}-\d{2}-\d{4}$"
    if not re.match(date_format, date):
        return False
    month, day, year = map(int, date.split('-'))
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False
    elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(valid_date('03-11-2000'))
        self.assertFalse(valid_date('15-01-2012'))
        self.assertFalse(valid_date('04-0-2040'))
        self.assertTrue(valid_date('06-04-2020'))
        self.assertFalse(valid_date('06/04/2020'))

if __name__ == '__main__':
    unittest.main()