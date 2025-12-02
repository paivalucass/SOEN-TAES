def valid_date(date):
    if len(date) != 10:
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    if not all(char.isdigit() for char in date[:2]) or not all(char.isdigit() for char in date[3:5]) or not all(char.isdigit() for char in date[6:]):
        return False
    
    month, day, year = int(date[:2]), int(date[3:5]), int(date[6:])
    
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    else:  # February
        if year % 4 == 0:  # Leap year
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