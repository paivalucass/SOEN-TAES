def check_monthnumb_number(monthnum2):
    month_days_mapping = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if monthnum2 < 1 or monthnum2 > 12:
        raise ValueError("Invalid month number")

    if month_days_mapping[monthnum2] == 31:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumb_number(5), True)

if __name__ == '__main__':
    unittest.main()