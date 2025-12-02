def even_bit_set_number(n):
    if not isinstance(n, int):
        raise ValueError("Input parameter 'n' must be a valid integer")
    
    if n % 2 != 0:
        return n | 0b1010101010101010
    else:
        return n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_bit_set_number(10), 10)

if __name__ == '__main__':
    unittest.main()