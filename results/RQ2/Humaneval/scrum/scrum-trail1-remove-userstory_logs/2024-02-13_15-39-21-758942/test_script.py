def order_by_points(nums):
    def calculate_digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    def sort_key(item):
        return (calculate_digit_sum(item), nums.index(item))

    return sorted(nums, key=sort_key)
import unittest

class Test(unittest.TestCase):
    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()