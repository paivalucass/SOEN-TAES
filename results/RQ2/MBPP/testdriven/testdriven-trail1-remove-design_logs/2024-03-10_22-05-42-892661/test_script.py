def set_left_most_unset_bit(number):
    '''Write a python function to set the left most unset bit.
    assert set_left_most_unset_bit(10) == 14
    '''
    if number <= 0:
        return 1
    else:
        binary_number = bin(number)[2:]
        if '0' not in binary_number:
            return number
        else:
            unset_index = binary_number.index('0')
            return number + 2 ** (len(binary_number) - unset_index - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_left_most_unset_bit(10), 14)

if __name__ == '__main__':
    unittest.main()