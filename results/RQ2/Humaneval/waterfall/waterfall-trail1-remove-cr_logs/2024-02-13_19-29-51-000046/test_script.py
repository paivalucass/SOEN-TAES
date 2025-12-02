def order_by_points(nums):
    def digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()