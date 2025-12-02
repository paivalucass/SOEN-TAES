def even_bit_set_number(n):
    if type(n) != int or n < 0:
        raise ValueError("Input should be a non-negative integer")
    result = 0
    bit_position = 0
    while n > 0:
        if bit_position % 2 != 0:
            result |= (n & 1) << bit_position
        n >>= 1
        bit_position += 1
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_bit_set_number(10), 10)

if __name__ == '__main__':
    unittest.main()