import datetime

def valid_date(date):
    try:
        date_format = '%m-%d-%Y'
        datetime.datetime.strptime(date, date_format)
        month, day, year = map(int, date.split('-'))
        if month < 1 or month > 12 or day < 1:
            return False
        elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
            return False
        elif month in [4, 6, 9, 11] and day > 30:
            return False
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                if day > 29:
                    return False
            elif day > 28:
                return False
        return True
    except ValueError:
        return False
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