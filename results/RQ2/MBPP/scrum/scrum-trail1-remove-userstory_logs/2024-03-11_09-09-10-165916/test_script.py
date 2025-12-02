def rearrange_bigger(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid Input"

    digits = [int(d) for d in str(n)]

    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            min_index = i + 1
            for j in range(i + 2, len(digits)):
                if digits[j] > digits[i] and digits[j] < digits[min_index]:
                    min_index = j
            digits[i], digits[min_index] = digits[min_index], digits[i]
            digits[i + 1:] = sorted(digits[i + 1:])
            return int(''.join(map(str, digits)))

    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()