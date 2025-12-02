def circular_shift(x, shift):
    if not isinstance(x, int) or not isinstance(shift, int) or shift < 0:
        return "Invalid input"
    
    x_str = str(x)

    def shift_digits(shift_amount):
        return x_str[-shift_amount:] + x_str[:-shift_amount]

    if shift > 0:
        shift %= len(x_str)
        return shift_digits(shift)
    elif shift < 0:
        shift = -shift % len(x_str)
        return shift_digits(shift)
    else:
        return x_str

import unittest

class Test(unittest.TestCase):
    def test_circular_shift(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12, 2), "12")

if __name__ == '__main__':
    unittest.main()