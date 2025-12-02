def order_by_points(nums):
    def digit_sum(num):
        if num < 0:
            num = -num
        return sum(int(digit) for digit in str(num))

    nums.sort(key=lambda x: (digit_sum(x), nums.index(x)))
    return nums
import unittest

class Test(unittest.TestCase):
    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()