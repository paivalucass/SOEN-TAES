def check_monthnumb_number(monthnum2: int) -> bool:
    MONTHS_WITH_31_DAYS = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31}

    if not isinstance(monthnum2, int) or monthnum2 < 1 or monthnum2 > 12:
        raise ValueError("Invalid month number input")

    return monthnum2 in MONTHS_WITH_31_DAYS
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumb_number(5), True)

if __name__ == '__main__':
    unittest.main()