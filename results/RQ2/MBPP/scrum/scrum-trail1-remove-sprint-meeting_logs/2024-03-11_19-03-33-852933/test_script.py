def reverse_Array_Upto_K(input_array, position):
    if len(input_array) < 2 or position <= 0:
        return input_array

    if position > len(input_array):
        position = len(input_array)

    return input_array[:position][::-1] + input_array[position:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4), [4, 3, 2, 1, 5, 6])

if __name__ == '__main__':
    unittest.main()