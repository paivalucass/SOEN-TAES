def rearrange_bigger(n):
    if not isinstance(n, int):
        return "Input is not a number"

    if n < 0:
        return "Input should be a positive number"

    digits = [int(d) for d in str(n)]
    sorted_digits = sorted(digits, reverse=True)

    if sorted_digits == digits:
        return "No bigger number can be formed"

    for i in range(len(digits)-1, 0, -1):
        if digits[i] > digits[i-1]:
            temp = digits[i-1]
            min_index = i
            for j in range(i, len(digits)):
                if digits[j] > temp and digits[j] < digits[min_index]:
                    min_index = j
            digits[i-1] = digits[min_index]
            digits[min_index] = temp
            result = digits[:i] + sorted(digits[i:])
            break

    return int(''.join(map(str, result)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()