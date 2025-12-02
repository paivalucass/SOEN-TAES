def toggle_middle_bits(n):
    middle_bits = (n & 0xFFFFFFE0) >> 1
    return n ^ middle_bits

def set_middle_bits(n):  
    return toggle_middle_bits(n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()