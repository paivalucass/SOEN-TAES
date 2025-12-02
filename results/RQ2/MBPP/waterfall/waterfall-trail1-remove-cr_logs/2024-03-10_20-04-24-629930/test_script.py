def change_date_format(dt):
    if len(dt) != 10 or dt[4] != '-' or dt[7] != '-':
        return "Input date format is not valid (yyyy-mm-dd)"
    else:
        new_date = dt[8:] + '-' + dt[5:7] + '-' + dt[:4]
        return new_date
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(change_date_format('2026-01-02'), '02-01-2026')

if __name__ == '__main__':
    unittest.main()