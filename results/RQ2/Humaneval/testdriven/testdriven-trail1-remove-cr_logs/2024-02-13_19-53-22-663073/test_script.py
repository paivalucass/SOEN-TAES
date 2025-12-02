def order_by_points(nums):
    if not isinstance(nums, list):
        return "Invalid input"

    if len(nums) == 0:
        return []

    def get_sum_of_digits(n):
        return sum(int(digit) for digit in str(abs(n)))

    def custom_sort(n):
        return (get_sum_of_digits(n), nums.index(n))

    return sorted(nums, key=custom_sort)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()