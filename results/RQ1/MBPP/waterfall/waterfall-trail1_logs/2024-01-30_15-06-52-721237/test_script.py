def check_month_number(month_number):
    if month_number < 1 or month_number > 12:
        raise ValueError("Invalid month number. Please provide a number between 1 and 12.")

    days_in_each_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    return days_in_each_month[month_number] == 30
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()