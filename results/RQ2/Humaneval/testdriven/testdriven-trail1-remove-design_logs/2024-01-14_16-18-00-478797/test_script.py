def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    # Input validation checks
    if x < 0 or base < 2 or base >= 10:
        raise ValueError("Base number must be less than 10 and greater than 1")

    result = ""

    # Conversion logic
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base

    # Return result
    return result if result else "0"
import unittest

class Test(unittest.TestCase):
    def test_change_base_1(self):
        self.assertEqual(change_base(8, 3), '22')

    def test_change_base_2(self):
        self.assertEqual(change_base(8, 2), '1000')

    def test_change_base_3(self):
        self.assertEqual(change_base(7, 2), '111')

    def test_invalid_base(self):
        with self.assertRaises(ValueError):
            change_base(8, 10)

if __name__ == '__main__':
    unittest.main()