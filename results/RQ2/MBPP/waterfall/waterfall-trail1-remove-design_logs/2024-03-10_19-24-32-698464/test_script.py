def divisible_by_digits(startnum, endnum):
    divisible_numbers = []
    for number in range(startnum, endnum + 1):
        digits = [int(digit) for digit in str(number) if int(digit) != 0 and number % int(digit) == 0]
        if len(digits) == len(str(number)):
            divisible_numbers.append(number)
    return divisible_numbers
import unittest

class Test(unittest.TestCase):
    def test_divisible_by_digits(self):
        self.assertEqual(divisible_by_digits(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

if __name__ == '__main__':
    unittest.main()