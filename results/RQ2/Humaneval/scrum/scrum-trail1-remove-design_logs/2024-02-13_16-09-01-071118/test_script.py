def circular_shift(x, shift):
    if not isinstance(x, int) or not isinstance(shift, int):
        raise ValueError("x and shift must be integers")
    if x < 0 or shift < 0:
        raise ValueError("x and shift must be positive integers")
    
    x_str = str(x)
    num_digits = len(x_str)
    shift = shift % num_digits
    if shift == 0:
        return x_str
    else:
        return x_str[-shift:] + x_str[:-shift]

def count_digits(x):
    return len(str(x))
import unittest

class Test(unittest.TestCase):
    def test_circular_shift_1(self):
        self.assertEqual(circular_shift(12, 1), "21")

    def test_circular_shift_2(self):
        self.assertEqual(circular_shift(12, 2), "12")

if __name__ == '__main__':
    unittest.main()