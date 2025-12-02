def circular_shift(x, shift):
    x_str = str(x)
    num_digits = len(x_str)
    shift = shift % num_digits
    if shift == 0:
        return x_str
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]
        return shifted_str if shift <= num_digits else x_str[::-1]
import unittest

class Test(unittest.TestCase):
    def test_circular_shift_1(self):
        self.assertEqual(circular_shift(12, 1), "21")
    
    def test_circular_shift_2(self):
        self.assertEqual(circular_shift(12, 2), "12")

if __name__ == '__main__':
    unittest.main()