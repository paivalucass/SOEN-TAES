def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if x < 0 or base < 0:
        raise ValueError("x and base must be positive integers")

    result = ''
    if x == 0:
        return '0'
    while x > 0:
        result = str(x % base) + result
        x = x // base
    return result
import unittest

class Test(unittest.TestCase):
    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(10, 2), '1010')

if __name__ == '__main__':
    unittest.main()