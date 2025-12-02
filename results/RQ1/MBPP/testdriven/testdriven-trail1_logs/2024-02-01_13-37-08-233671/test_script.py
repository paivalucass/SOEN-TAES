def check_monthnumber_number(monthnum3):
    MONTH_DAYS = {
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

    if not isinstance(monthnum3, int):
        return "Error"
    elif monthnum3 < 1 or monthnum3 > 12:
        return False
    else:
        if MONTH_DAYS[monthnum3] == 30:
            return True
        else:
            return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()