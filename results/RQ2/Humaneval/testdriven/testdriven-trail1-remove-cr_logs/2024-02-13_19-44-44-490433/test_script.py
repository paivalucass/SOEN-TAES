def change_base(x: int, base: int):
    # check if base is less than 2 or greater than 10
    if base < 2 or base > 10:
        return "Error: Base number should be between 2 and 10"

    # check if x is negative
    if x < 0:
        return "Error: Input number should be non-negative"

    # check if x is not an integer
    if not isinstance(x, int):
        return "Error: Input number should be an integer"

    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result
import unittest

class Test(unittest.TestCase):
    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')

if __name__ == '__main__':
    unittest.main()