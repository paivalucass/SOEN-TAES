def check_monthnumb_number(monthnum2):
    if not isinstance(monthnum2, int) or monthnum2 < 1 or monthnum2 > 12:
        return "Error: Invalid input. Please provide a valid integer between 1 and 12."

    if monthnum2 in [1, 3, 5, 7, 8, 10, 12]:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumb_number(5), True)

if __name__ == '__main__':
    unittest.main()