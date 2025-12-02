def is_decimal(num):
    try:
        float_num = float(num)
        decimal_num = round(float_num, 2)
        if float_num == decimal_num:
            return True
        else:
            return False
    except:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_decimal('123.11'), True)

if __name__ == '__main__':
    unittest.main()