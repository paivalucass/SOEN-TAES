def reverse_Array_Upto_K(input, k):
    if not isinstance(input, list):
        raise ValueError('Input is not a valid array')
    if not isinstance(k, int) or k < 0 or k >= len(input):
        raise ValueError('k is not a valid position')

    reversed_part = input[:k][::-1]
    remaining_part = input[k:]
    reversed_arr = reversed_part + remaining_part
    return reversed_arr
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4), [4, 3, 2, 1, 5, 6])

if __name__ == '__main__':
    unittest.main()