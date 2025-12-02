def even_bit_set_number(n):
    if not isinstance(n, int):
        return "Error: Non-numeric input"
    
    if n < 0:
        raise ValueError("Input number must be positive")

    mask = 0xaaaaaaaa  # Mask to set even bits to 1
    result = n & mask  # Bitwise AND operation to set even bits to 1
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_bit_set_number(10), 10)

if __name__ == '__main__':
    unittest.main()