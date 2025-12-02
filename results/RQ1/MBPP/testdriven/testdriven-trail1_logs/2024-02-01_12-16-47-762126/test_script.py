def even_bit_set_number(n):
    """
    Design a Python function to set all even bits of a given number to 1.

    Args:
    - n: An integer number. It is assumed that the input number can be any integer.

    Returns:
    - The modified number with all even bits set to 1
    """
    return n & 0b1010101010101010
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_bit_set_number(10), 10)

if __name__ == '__main__':
    unittest.main()