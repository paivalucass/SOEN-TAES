def validate(n):
    '''Check whether the frequency of each digit in the integer is less than or equal to the digit itself.'''
    digit_count = {}
    for digit in str(n):
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    for digit, count in digit_count.items():
        if int(digit) < count:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(validate(1234), True)

if __name__ == '__main__':
    unittest.main()