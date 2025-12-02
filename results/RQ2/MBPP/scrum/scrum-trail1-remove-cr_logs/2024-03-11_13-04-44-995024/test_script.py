def validate(n):
    if isinstance(n, int):
        digit_count = {}
        for digit in str(n):
            if digit.isdigit():
                if int(digit) in digit_count:
                    digit_count[int(digit)] += 1
                else:
                    digit_count[int(digit)] = 1
        for key, value in digit_count.items():
            if key != 0 and value > key:
                return False
        return True
    else:
        raise ValueError("Input must be an integer")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(validate(1234))

if __name__ == '__main__':
    unittest.main()