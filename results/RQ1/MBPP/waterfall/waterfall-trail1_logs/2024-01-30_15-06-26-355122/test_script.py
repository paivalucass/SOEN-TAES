def is_decimal(num):
    try:
        num = float(num)
        if isinstance(num, float) and round(num, 2) == num:
            return True
        else:
            return False
    except ValueError:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_decimal('123.11'), True)

if __name__ == '__main__':
    unittest.main()