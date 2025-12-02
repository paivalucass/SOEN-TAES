def even_bit_set_number(n):
    mask = 0xAAAAAAAA
    result = n & mask
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_bit_set_number(10), 10)

if __name__ == '__main__':
    unittest.main()