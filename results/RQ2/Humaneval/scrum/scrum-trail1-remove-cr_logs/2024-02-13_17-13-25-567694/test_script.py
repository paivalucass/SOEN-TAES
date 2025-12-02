def valid_date(date):
    import re
    import datetime
    
    def validate_input_format(date):
        pattern = r'^\d{2}-\d{2}-\d{4}$'
        return bool(re.match(pattern, date))

    def validate_date(date):
        try:
            month, day, year = map(int, date.split('-'))
            if month < 1 or month > 12:
                return False
            if day < 1 or day > 31:
                return False
            if month in [4, 6, 9, 11] and day > 30:
                return False
            if month == 2 and day > 29:
                return False
            if month == 2 and day == 29 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
                return False
            return True
        except ValueError:
            return False

    if date == "":
        return False
    if not validate_input_format(date):
        return False
    if not validate_date(date):
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