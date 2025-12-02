from decimal import Decimal, InvalidOperation

def is_decimal(num):
    try:
        decimal_number = Decimal(num)
        if len(decimal_number.as_tuple().digits) - decimal_number.as_tuple().exponent - 1 > 2:
            return False
        return True
    except (ValueError, InvalidOperation):
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_decimal('123.11'), True)

if __name__ == '__main__':
    unittest.main()