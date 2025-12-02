def circular_shift(x, shift):
    if not isinstance(x, int) or not isinstance(shift, int) or shift == 0:
        return "Invalid input"
    
    x_str = str(x)
    n = len(x_str)
    
    shift = shift % n
    if shift == 0:
        return x_str
    
    result = x_str[-shift:] + x_str[:-shift]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_circular_shift(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12, 2), "12")
        self.assertEqual(circular_shift(12345, 3), "34512")
        self.assertEqual(circular_shift(12345, 10), "54321")

if __name__ == '__main__':
    unittest.main()