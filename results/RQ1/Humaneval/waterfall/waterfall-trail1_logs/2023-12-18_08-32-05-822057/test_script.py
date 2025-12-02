def order_by_points(nums):
    if not isinstance(nums, list) or not all(isinstance(i, int) for i in nums):
        raise ValueError("Input must be a list of integers")

    def calculate_digit_sum(num):
        if num < 0:
            num = -num
        sum_digit = 0
        for digit in str(num):
            if digit.isdigit():
                sum_digit += int(digit)
        return sum_digit, num

    return sorted(nums, key=lambda x: calculate_digit_sum(x))
import unittest

class Test(unittest.TestCase):
    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()