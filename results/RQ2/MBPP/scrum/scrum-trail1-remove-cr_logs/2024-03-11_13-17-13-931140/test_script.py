def change_date_format(dt):
    # Split the date string by '-' and then re-arrange the elements
    # to form the new date format
    date_list = dt.split('-')
    return f'{date_list[2]}-{date_list[1]}-{date_list[0]}'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(change_date_format("2026-01-02"), '02-01-2026')

if __name__ == '__main__':
    unittest.main()