def check_month_number(month_number):
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    try:
        month = int(month_number)
        if month < 1 or month > 12:
            return "Invalid Input"
        else:
            if month in [4, 6, 9, 11]:
                return True
            elif month == 2:
                return "28 or 29 days"
            else:
                return False
    except ValueError:
        return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_monthnumber_number(6), True)

if __name__ == '__main__':
    unittest.main()