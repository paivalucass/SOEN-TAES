def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base >= 10:
        raise ValueError("Base must be less than 10")

    if x == 0:
        return '0'

    if x < 0:
        is_negative = True
        x = abs(x)
    else:
        is_negative = False

    result = ''
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base

    if is_negative:
        result = '-' + result

    return result
import unittest

class Test(unittest.TestCase):
    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')

if __name__ == '__main__':
    unittest.main()