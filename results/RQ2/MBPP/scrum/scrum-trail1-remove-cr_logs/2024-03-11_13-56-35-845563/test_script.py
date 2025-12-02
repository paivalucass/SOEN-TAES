def toggle_middle_bits(n):
    bits = 1
    while bits <= n:
        bits = bits << 1
    return ((bits - 1) ^ n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()