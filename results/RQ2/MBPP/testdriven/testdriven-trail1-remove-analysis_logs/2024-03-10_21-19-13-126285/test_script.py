def change_date_format(dt):
    try:
        from datetime import datetime
        input_date = datetime.strptime(dt, '%Y-%m-%d')
        return input_date.strftime('%d-%m-%Y')
    except ValueError:
        return "Invalid input date format"

assert change_date_format("2026-01-02") == '02-01-2026'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(change_date_format('2026-01-02'), '02-01-2026')

if __name__ == '__main__':
    unittest.main()