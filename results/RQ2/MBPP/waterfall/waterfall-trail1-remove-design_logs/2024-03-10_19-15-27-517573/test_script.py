def change_date_format(dt):
    try:
        date_parts = dt.split('-')
        formatted_date = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
        return formatted_date
    except IndexError:
        return "Error Message"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(change_date_format('2026-01-02'), '02-01-2026')

if __name__ == '__main__':
    unittest.main()