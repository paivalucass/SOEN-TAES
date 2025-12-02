def circular_shift(x, shift):
    if not isinstance(x, int) or not isinstance(shift, int):
        return "Error: Input values must be integers"
    if shift < 0:
        return "Error: Shift value must be a non-negative integer"

    x_str = str(x)
    if shift > len(x_str):
        return x_str[::-1]

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