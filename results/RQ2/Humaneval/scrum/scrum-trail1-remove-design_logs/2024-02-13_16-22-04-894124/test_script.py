def valid_date(date):
    if '/' in date:
        return False
    month, day, year = date.split('-')
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    if int(month) < 1 or int(month) > 12:
        return False
    if int(day) < 1 or int(day) > 31:
        return False
    if int(month) in [4, 6, 9, 11] and int(day) > 30:
        return False
    if int(month) == 2 and int(day) > 29:
        return False
    if int(month) == 2 and int(day) == 29:
        if int(year) % 4 != 0:
            return False
        elif int(year) % 100 == 0 and int(year) % 400 != 0:
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