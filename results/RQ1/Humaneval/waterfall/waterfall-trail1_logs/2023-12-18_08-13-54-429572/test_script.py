def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int) or x < 0 or base < 2 or base > 9:
        raise ValueError("Invalid input: x and base should be positive integers, and base should be between 2 and 9.")

    result = ''
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result

# Unit tests
assert change_base(8, 3) == '22'
assert change_base(8, 2) == '1000'
assert change_base(7, 2) == '111'
import unittest

class Test(unittest.TestCase):
    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')

if __name__ == '__main__':
    unittest.main()