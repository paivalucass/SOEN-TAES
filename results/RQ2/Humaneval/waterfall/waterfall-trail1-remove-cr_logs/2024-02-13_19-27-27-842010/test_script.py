import re

def valid_date(date):
    if not re.match(r'\d{2}-\d{2}-\d{4}', date):
        return False
    
    month, day, year = map(int, date.split('-'))
    
    if month < 1 or month > 12:
        return False
    
    if (month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31)) or (month in [4, 6, 9, 11] and (day < 1 or day > 30)) or (month == 2 and (day < 1 or (day > 29 and year % 4 == 0) or (day > 28 and year % 4 != 0))):
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