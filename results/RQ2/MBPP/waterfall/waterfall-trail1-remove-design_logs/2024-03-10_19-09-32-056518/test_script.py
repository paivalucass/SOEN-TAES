def even_bit_set_number(n):
    # Set all even bits of the given number
    return n & 0xAA
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_bit_set_number(10), 10)

if __name__ == '__main__':
    unittest.main()