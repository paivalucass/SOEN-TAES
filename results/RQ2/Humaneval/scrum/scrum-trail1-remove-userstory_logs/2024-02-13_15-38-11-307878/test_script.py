def order_by_points(nums):
    def calculate_sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    return sorted(nums, key=lambda x: (calculate_sum_of_digits(x), nums.index(x))) if nums else []
import unittest

class Test(unittest.TestCase):
    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()