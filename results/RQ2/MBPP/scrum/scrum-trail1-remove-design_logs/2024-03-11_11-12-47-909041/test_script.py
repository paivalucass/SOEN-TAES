def is_decimal(num):
    '''
    Write a function to check whether a given string is a decimal number with a precision of 2.
    assert is_decimal('123.11')==True
    '''
    try:
        float_num = float(num)
        if round(float_num, 2) == float_num:
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