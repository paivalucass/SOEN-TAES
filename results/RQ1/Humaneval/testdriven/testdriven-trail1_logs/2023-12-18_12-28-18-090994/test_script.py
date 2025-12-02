def circular_shift(x, shift):
    try:
        if not isinstance(x, int) or x < 0:
            raise ValueError("Error: Invalid input for x")
        if not isinstance(shift, int) or shift < 0:
            raise ValueError("Error: Invalid input for shift")
        
        x_str = str(x)
        num_digits = len(x_str)
        
        if shift > num_digits:
            return x_str[::-1]
        
        shift = shift % num_digits  # Fix for handling shift greater than number of digits
        
        return x_str[-shift:] + x_str[:-shift]
    
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test_circular_shift_1(self):
        self.assertEqual(circular_shift(12, 1), "21")
    
    def test_circular_shift_2(self):
        self.assertEqual(circular_shift(12, 2), "12")

    def test_circular_shift_3(self):
        self.assertEqual(circular_shift(12345, 3), "34512")

    def test_circular_shift_4(self):
        self.assertEqual(circular_shift(12345, 6), "12345")

if __name__ == '__main__':
    unittest.main()