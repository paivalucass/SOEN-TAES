def divisible_by_digits(startnum, endnum):
    result = []

    if startnum < 0 or endnum < 0 or startnum > endnum:
        return "Invalid input"

    for num in range(startnum, endnum + 1):
        digits = [int(digit) for digit in str(num)]
        if all(digit != 0 and num % digit == 0 for digit in digits):
            result.append(num)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisible_by_digits(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

if __name__ == '__main__':
    unittest.main()