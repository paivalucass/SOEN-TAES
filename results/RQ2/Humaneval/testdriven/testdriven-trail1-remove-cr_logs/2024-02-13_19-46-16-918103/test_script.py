def circular_shift(x, shift):
    if not isinstance(x, int) or not isinstance(shift, int):
        raise ValueError("Inputs must be valid integers")
    
    if shift < 0:
        raise ValueError("Shift value must be non-negative")
    
    x_str = str(x)
    num_digits = len(x_str)
    
    if shift > num_digits:
        return x_str[::-1]
    
    shifted_str = x_str[-shift:] + x_str[:-shift]
    return shifted_str
import unittest

class Test(unittest.TestCase):
    def test_circular_shift_1(self):
        self.assertEqual(circular_shift(12, 1), "21")

    def test_circular_shift_2(self):
        self.assertEqual(circular_shift(12, 2), "12")

if __name__ == '__main__':
    unittest.main()