def change_base(x: int, base: int):
    if x == 0 or base == 1:
        return "Invalid input"

    result = ""
    if x < 0:
        is_negative = True
        x = abs(x)
    else:
        is_negative = False

    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base

    if is_negative:
        result = "-" + result

    return result
import unittest

class Test(unittest.TestCase):
    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')

if __name__ == '__main__':
    unittest.main()