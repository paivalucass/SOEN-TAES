def change_base(x: int, base: int):
    if x < 0 or base < 2:
        return 'Invalid input'
    result = ''
    while x > 0:
        result = str(x % base) + result
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

    def test_change_base_invalid_input(self):
        self.assertEqual(change_base(-5, 3), 'Invalid input')

if __name__ == '__main__':
    unittest.main()