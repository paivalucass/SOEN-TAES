def circular_shift(x, shift):
    x = str(x)
    n = len(x)
    if shift % n == 0:
        return x
    elif shift > n:
        return x[::-1]
    else:
        shift %= n
        return x[n - shift:] + x[:n - shift]
import unittest

class TestCircularShift(unittest.TestCase):
    def test_shift_by_one(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(123, 1), "312")
        self.assertEqual(circular_shift(1234, 1), "4123")

    def test_shift_by_two(self):
        self.assertEqual(circular_shift(12, 2), "12")
        self.assertEqual(circular_shift(123, 2), "231")
        self.assertEqual(circular_shift(1234, 2), "3412")

    def test_shift_greater_than_length(self):
        self.assertEqual(circular_shift(12, 3), "21")
        self.assertEqual(circular_shift(123, 4), "321")
        self.assertEqual(circular_shift(1234, 5), "4321")

if __name__ == '__main__':
    unittest.main()