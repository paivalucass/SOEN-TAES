def circular_shift(x, shift):
    # Input validation
    if not isinstance(x, int) or not isinstance(shift, int):
        return "Invalid input: x and shift must be integers"

    # Handle edge case where shift is greater than the number of digits in x
    x_str = str(x)
    if abs(shift) > len(x_str):
        return x_str[::-1]

    # Circular shift the digits of x
    shifted_digits = x_str[-shift:] + x_str[:-shift]
    return shifted_digits
import unittest

class TestCircularShift(unittest.TestCase):
    def test_circular_shift_1(self):
        self.assertEqual(circular_shift(12, 1), "21")

    def test_circular_shift_2(self):
        self.assertEqual(circular_shift(12, 2), "12")

if __name__ == '__main__':
    unittest.main()