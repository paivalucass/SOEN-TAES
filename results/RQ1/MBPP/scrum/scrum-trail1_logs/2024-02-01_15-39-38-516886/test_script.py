import datetime

def change_date_format(dt):
    date_obj = datetime.datetime.strptime(dt, '%Y-%m-%d')
    return date_obj.strftime('%d-%m-%Y')
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(change_date_format('2026-01-02'), '02-01-2026')

if __name__ == '__main__':
    unittest.main()