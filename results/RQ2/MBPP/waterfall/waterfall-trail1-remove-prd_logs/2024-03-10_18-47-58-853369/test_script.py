def check_monthnumber_number(month_num):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month_num < 1 or month_num > 12:
        raise ValueError("Month number must be between 1 and 12")
    
    return days_in_month[month_num - 1] == 30
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()