def circular_shift(x, shift):
    if not isinstance(x, int) or x <= 0:
        return "Invalid input for x. Please provide a positive integer."

    if not isinstance(shift, int) or shift < 0:
        return "Invalid input for shift. Please provide a non-negative integer."

    x_str = str(x)
    if len(x_str) == 1 or shift == 0:
        return x_str

    shift = shift % len(x_str)
    result = x_str[-shift:] + x_str[:-shift]

    return result
import unittest

class Test(unittest.TestCase):
    def test_circular_shift_1(self):
        self.assertEqual(circular_shift(12, 1), "21")

    def test_circular_shift_2(self):
        self.assertEqual(circular_shift(12, 2), "12")

if __name__ == '__main__':
    unittest.main()