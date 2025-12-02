def rearrange_bigger(n):
    digits = [int(d) for d in str(n)]
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i == -1:
        return "No bigger number can be formed"
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = digits[i + 1:][::-1]
    result = int(''.join(map(str, digits)))
    return result if result > n else "No bigger number can be formed"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()