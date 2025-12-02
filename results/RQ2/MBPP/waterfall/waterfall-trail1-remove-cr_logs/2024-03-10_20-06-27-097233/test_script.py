def check_monthnumb_number(month_number):
    if not 1 <= month_number <= 12:
        return False
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    return month_number in months_with_31_days
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumb_number(5), True)

if __name__ == '__main__':
    unittest.main()