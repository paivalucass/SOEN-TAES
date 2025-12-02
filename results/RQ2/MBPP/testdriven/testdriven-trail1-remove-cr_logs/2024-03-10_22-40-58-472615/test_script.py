def change_date_format(dt):
    '''Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.'''
    try:
        datetime.datetime.strptime(dt, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be yyyy-mm-dd")
    new_date = datetime.datetime.strptime(dt, '%Y-%m-%d').strftime('%d-%m-%Y')
    return new_date
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(change_date_format("2026-01-02"), '02-01-2026')

if __name__ == '__main__':
    unittest.main()