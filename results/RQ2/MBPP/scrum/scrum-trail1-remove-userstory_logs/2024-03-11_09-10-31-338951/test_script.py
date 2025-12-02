def change_date_format(dt):
    try:
        if not isinstance(dt, str) or len(dt) != 10 or dt[4] != '-' or dt[7] != '-':
            raise ValueError("Invalid input date format")

        output_date = dt[8:] + '-' + dt[5:7] + '-' + dt[:4]
        return output_date
    except ValueError as ve:
        return "Error: Invalid date format"
    except Exception as e:
        return "An error occurred: " + str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(change_date_format('2026-01-02'), '02-01-2026')

if __name__ == '__main__':
    unittest.main()