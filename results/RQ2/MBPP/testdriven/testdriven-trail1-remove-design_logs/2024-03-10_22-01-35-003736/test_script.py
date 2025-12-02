def even_bit_set_number(n):
    '''
    Write a python function to set all even bits of a given number.
    assert even_bit_set_number(10) == 10
    '''
    return n & 0xAAAAAAAA  # Mask to set all even bits
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_bit_set_number(10), 10)

if __name__ == '__main__':
    unittest.main()