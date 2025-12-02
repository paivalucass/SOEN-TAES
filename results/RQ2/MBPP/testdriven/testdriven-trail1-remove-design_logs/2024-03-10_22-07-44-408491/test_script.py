import datetime

def change_date_format(dt):
    try:
        formatted_date = datetime.datetime.strptime(dt, '%Y-%m-%d').strftime('%d-%m-%Y')
        return formatted_date
    except ValueError:
        return "Error: Invalid date format"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(change_date_format("2026-01-02"), '02-01-2026')

if __name__ == '__main__':
    unittest.main()