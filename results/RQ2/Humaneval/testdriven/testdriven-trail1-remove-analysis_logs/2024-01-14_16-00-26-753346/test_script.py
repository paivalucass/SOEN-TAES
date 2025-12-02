def order_by_points(nums):
    nums.sort(key=lambda x: (sum(int(digit) for digit in str(abs(x))), nums.index(x) if x in nums else -1))
    return nums
import unittest

class Test(unittest.TestCase):
    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()