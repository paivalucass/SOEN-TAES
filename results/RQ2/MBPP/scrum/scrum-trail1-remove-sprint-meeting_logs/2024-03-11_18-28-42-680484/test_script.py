def even_bit_set_number(n): 
    mask = 0xAAAAAAAA  # Mask with alternating 1s at even positions
    return n & mask
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_bit_set_number(10), 10)

if __name__ == '__main__':
    unittest.main()