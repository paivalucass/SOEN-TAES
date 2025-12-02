def order_by_points(nums):
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise ValueError("Input must be a list of integers")

    def sum_of_digits(num):
        if num < 0:
            num = -num
        total = 0
        while num:
            total += num % 10
            num //= 10
        return total

    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))
import unittest

class Test(unittest.TestCase):
    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()