def sum_digits(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Input must be a non-negative integer")

    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    digit_sum = 0
    for digit in str(n):
        digit_sum += int(digit)

    return digit_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_digits(345), 12)

if __name__ == '__main__':
    unittest.main()