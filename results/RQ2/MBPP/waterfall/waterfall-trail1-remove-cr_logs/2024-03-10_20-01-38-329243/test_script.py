def set_left_most_unset_bit(n):
    unset_bit = next((i for i in range(32) if (n >> i) & 1 == 0), None)
    if unset_bit is None:
        raise ValueError('Input must be a positive integer')
    modified_integer = n | (1 << unset_bit)
    return modified_integer
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_left_most_unset_bit(10), 14)

if __name__ == '__main__':
    unittest.main()