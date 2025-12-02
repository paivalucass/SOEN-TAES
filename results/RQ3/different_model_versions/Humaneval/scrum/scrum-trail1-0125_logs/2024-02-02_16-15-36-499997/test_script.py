def change_base(x: int, base: int):
    result = ''
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result.strip()
import unittest

class Test(unittest.TestCase):
    
    def test_change_base_3(self):
        self.assertEqual(change_base(8, 3), '22')

    def test_change_base_2(self):
        self.assertEqual(change_base(8, 2), '1000')

    def test_change_base_4(self):
        self.assertEqual(change_base(7, 2), '111')

if __name__ == '__main__':
    unittest.main()