def sum_of_digits(nums):
    sums = []
    for num in nums:
        if not isinstance(num, int):
            raise ValueError("Input must be an integer")
        sums.append(compute_sum_of_digits(num))
    return sums

def compute_sum_of_digits(num):
    digit_sum = 0
    num = abs(num)
    while num > 0:
        digit_sum += num % 10
        num = num // 10
    return digit_sum

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_of_digits([10, 2, 56]), 14)

if __name__ == '__main__':
    unittest.main()