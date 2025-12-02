def check_monthnumb_number(monthnum2):
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    if monthnum2 in [1, 3, 5, 7, 8, 10, 12]:
        return True
    elif monthnum2 in [4, 6, 9, 11]:
        return False
    else:
        return "Error: Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumb_number(5), True)

if __name__ == '__main__':
    unittest.main()