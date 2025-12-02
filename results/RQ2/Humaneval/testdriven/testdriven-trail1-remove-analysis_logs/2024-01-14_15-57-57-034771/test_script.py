import re

def valid_date(date):
    pattern = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$"
    if re.match(pattern, date) is None:
        return False
    month, day, year = map(int, date.split('-'))
    
    if month in [4,6,9,11] and day > 30:
        return False
    if month == 2 and day > 29:
        return False
    if month == 2 and day == 29 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
        return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(valid_date('03-11-2000'), True)
        self.assertEqual(valid_date('15-01-2012'), False)
        self.assertEqual(valid_date('04-0-2040'), False)
        self.assertEqual(valid_date('06-04-2020'), True)
        self.assertEqual(valid_date('06/04/2020'), False)

if __name__ == '__main__':
    unittest.main()