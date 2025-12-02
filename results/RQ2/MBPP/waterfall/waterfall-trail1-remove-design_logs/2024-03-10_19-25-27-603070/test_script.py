def is_decimal(num):
    try:
        float_value = float(num)
        return round(float_value, 2) == float_value
    except ValueError:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_decimal('123.11'), True)

if __name__ == '__main__':
    unittest.main()