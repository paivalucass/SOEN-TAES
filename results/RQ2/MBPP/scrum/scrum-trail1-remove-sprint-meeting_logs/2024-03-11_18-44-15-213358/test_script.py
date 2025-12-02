def change_date_format(dt):
    try:
        rearranged_date = dt.split('-')
        rearranged_date = rearranged_date[2] + '-' + rearranged_date[1] + '-' + rearranged_date[0]
        return rearranged_date
    except IndexError:
        return "Error handling for invalid date format"
    except Exception as e:
        return "Error handling for unexpected error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(change_date_format('2026-01-02'), '02-01-2026')

if __name__ == '__main__':
    unittest.main()