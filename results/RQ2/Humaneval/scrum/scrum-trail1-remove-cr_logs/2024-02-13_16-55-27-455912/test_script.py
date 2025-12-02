def change_base(x: int, base: int) -> str:
    if x < 0 or base < 2:
        return "Invalid input"
    
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