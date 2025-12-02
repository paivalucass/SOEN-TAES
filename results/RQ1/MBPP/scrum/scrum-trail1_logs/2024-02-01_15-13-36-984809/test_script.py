def validate(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    digit_freq = {}

    for digit in str(n):
        if digit in digit_freq:
            digit_freq[digit] += 1
        else:
            digit_freq[digit] = 1

    for digit, freq in digit_freq.items():
        if int(digit) < freq:
            return False

    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(validate(1234), True)

if __name__ == '__main__':
    unittest.main()