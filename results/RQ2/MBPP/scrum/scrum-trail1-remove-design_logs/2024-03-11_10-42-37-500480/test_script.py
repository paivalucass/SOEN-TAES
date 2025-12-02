def check_monthnumb_number(month_number: int) -> bool:
    month_days = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31}
    return month_number in month_days.keys()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumb_number(5), True)

if __name__ == '__main__':
    unittest.main()