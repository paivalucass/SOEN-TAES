def change_base(x: int, base: int) -> str:
    def convert_to_base(x: int, base: int) -> str:
        if x == 0:
            return ''
        else:
            return convert_to_base(x // base, base) + str(x % base)
    return convert_to_base(x, base)
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