def check_monthnumber_number(monthnum):
    if not isinstance(monthnum, int):
        raise ValueError("Invalid input")
    if monthnum < 1 or monthnum > 12:
        raise ValueError("Invalid month number. Month number should be between 1 and 12.")
    return monthnum in [4, 6, 9, 11]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()