def change_base(x: int, base: int):
    if not isinstance(x, int) or not isinstance(base, int) or base >= 10:
        return "Invalid input"

    if x < 0 or base < 2 or base > 9:
        return "Invalid input"

    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result
import unittest

class Test(unittest.TestCase):
    def test_change_base_1(self):
        self.assertEqual(change_base(8, 3), '22')

    def test_change_base_2(self):
        self.assertEqual(change_base(8, 2), '1000')

    def test_change_base_3(self):
        self.assertEqual(change_base(7, 2), '111')

if __name__ == '__main__':
    unittest.main()