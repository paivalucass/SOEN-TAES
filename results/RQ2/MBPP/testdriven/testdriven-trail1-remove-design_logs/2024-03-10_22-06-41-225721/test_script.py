def rearrange_bigger(n):
    '''
    Write a function to create the next bigger number by rearranging the digits of a given number.
    assert rearrange_bigger(12)==21
    '''
    n = str(n)
    if len(n) == 1:
        return "Invalid input"
    else:
        digits = list(n)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] > digits[i - 1]:
                temp = digits[i - 1]
                min_index = i
                for j in range(i, len(digits)):
                    if digits[j] > temp and digits[j] < digits[min_index]:
                        min_index = j
                digits[i - 1] = digits[min_index]
                digits[min_index] = temp
                result = int("".join(digits[:i] + sorted(digits[i:])))
                return result
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()