def rearrange_bigger(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    digits = [int(digit) for digit in str(n)]
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i < 0:
        return n
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i+1:] = sorted(digits[i+1:])
    return int(''.join(map(str, digits)))

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()