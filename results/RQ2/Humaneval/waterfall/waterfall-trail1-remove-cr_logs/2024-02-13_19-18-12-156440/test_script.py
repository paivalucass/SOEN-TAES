def change_base(x: int, base: int):
    if base > 10:
        return "Error: Base number should be less than 10"
    try:
        result = ""
        while x > 0:
            result = str(x % base) + result
            x = x // base
        return result
    except:
        return "Error: Invalid input number or base"
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