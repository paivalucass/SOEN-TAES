def change_date_format(dt):
    from datetime import datetime
    try:
        date_obj = datetime.strptime(dt, '%Y-%m-%d')
        return date_obj.strftime('%d-%m-%Y')
    except ValueError as e:
        print(f"Error occurred: {e}")
        return "01-01-1900"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(change_date_format('2026-01-02'), '02-01-2026')

if __name__ == '__main__':
    unittest.main()