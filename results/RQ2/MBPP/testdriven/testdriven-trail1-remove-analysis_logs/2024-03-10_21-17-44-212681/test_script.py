def sum_of_digits(nums):
    digit_sums = [sum(int(digit) for digit in str(num) if digit.isdigit()) for num in nums]
    return digit_sums
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_of_digits([10,2,56]), 14)

if __name__ == '__main__':
    unittest.main()