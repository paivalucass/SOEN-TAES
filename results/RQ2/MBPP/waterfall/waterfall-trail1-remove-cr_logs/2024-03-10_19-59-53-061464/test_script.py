def validate(n):
    n = abs(n)
    if not isinstance(n, int):
        raise ValueError("Input is not an integer")
    freq_dict = {}
    for digit in str(n):
        if digit in freq_dict:
            freq_dict[digit] += 1
        else:
            freq_dict[digit] = 1
    for digit, freq in freq_dict.items():
        if int(digit) < freq:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(validate(1234), True)

if __name__ == '__main__':
    unittest.main()