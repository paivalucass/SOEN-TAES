def valid_date(date):
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False
    month, day, year = map(int, date.split('-'))
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(valid_date('03-11-2000'), True)
        self.assertEqual(valid_date('15-01-2012'), False)
        self.assertEqual(valid_date('04-0-2040'), False)
        self.assertEqual(valid_date('06-04-2020'), True)
        self.assertEqual(valid_date('06/04/2020'), False)

if __name__ == '__main__':
    unittest.main()