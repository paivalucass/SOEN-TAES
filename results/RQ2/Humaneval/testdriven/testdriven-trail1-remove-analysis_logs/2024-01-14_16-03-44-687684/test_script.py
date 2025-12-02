def order_by_points(nums):
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(abs(n)))

    def sort_key(item):
        return (sum_of_digits(item), nums.index(item))

    nums.sort(key=sort_key)

    return nums
import unittest

class Test(unittest.TestCase):
    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()