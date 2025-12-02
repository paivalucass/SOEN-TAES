def toggle_middle_bits(n):
    mask = 0b01111110
    return n ^ mask
import unittest

class Test(unittest.TestCase):
    def test_toggle_middle_bits(self):
        self.assertEqual(toggle_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()