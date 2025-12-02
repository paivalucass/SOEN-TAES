def is_decimal(num):
    try:
        decimal_num = float(num)
        if '.' in num and len(num.split('.')[1]) == 2:
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