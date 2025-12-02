def even_bit_set_number(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Input should be a non-negative integer."

    bitmask = 0xAAAAAAAA  # This bitmask has all even bits set to 1
    result = n & bitmask  # Perform bitwise AND operation to set all even bits to 1

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_bit_set_number(10), 10)

if __name__ == '__main__':
    unittest.main()