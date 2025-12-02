def circular_shift(x, shift):
    if not isinstance(x, int) or not isinstance(shift, int):
        raise TypeError("Input parameters must be integers")
    
    if x < 0:
        return circular_shift(-x, shift)
    
    x_str = str(x)
    shift = shift % len(x_str)
    
    if shift == 0:
        return x_str
    else:
        return x_str[-shift:] + x_str[:-shift]
import unittest

class Test(unittest.TestCase):
    def test_circular_shift(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12, 2), "12")

if __name__ == '__main__':
    unittest.main()