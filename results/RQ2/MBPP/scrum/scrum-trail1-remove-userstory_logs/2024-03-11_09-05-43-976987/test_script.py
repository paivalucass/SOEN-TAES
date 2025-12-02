def count_digit_frequency(n):
    frequency = {}
    for digit in str(n):
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
    return frequency

def compare_frequency_with_digit(frequency):
    for digit, count in frequency.items():
        if int(digit) < count:
            return False
    return True

def validate(n):
    frequency = count_digit_frequency(n)
    return compare_frequency_with_digit(frequency)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(validate(1234), True)

if __name__ == '__main__':
    unittest.main()