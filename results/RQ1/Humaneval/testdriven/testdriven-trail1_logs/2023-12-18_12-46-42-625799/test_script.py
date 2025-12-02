def count_nums(arr):
    def sum_of_signed_digits(num):
        num = abs(num)
        total = 0
        while num > 0 or num < 0:
            total += num % 10
            num = num // 10
        return total

    def has_sum_of_signed_digits_greater_than_zero(num):
        return sum_of_signed_digits(num) > 0

    count = 0
    for num in arr:
        if has_sum_of_signed_digits_greater_than_zero(num):
            count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([]), 0)
        self.assertEqual(function_under_test([-1, 11, -11]), 1)
        self.assertEqual(function_under_test([1, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()