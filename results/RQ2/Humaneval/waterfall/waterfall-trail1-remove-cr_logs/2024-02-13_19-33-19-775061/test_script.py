def order_by_points(nums):
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All inputs must be integers")
    
    def digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    nums.sort(key=lambda x: (digit_sum(x), nums.index(x)))
    return nums

import unittest

class Test(unittest.TestCase):
    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()