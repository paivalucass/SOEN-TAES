def valid_date(date):
    try:
        month, day, year = map(int, date.split('-'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if year % 4 == 0:
                if day > 29:
                    return False
            else:
                if day > 28:
                    return False
        return True
    except:
        return False
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