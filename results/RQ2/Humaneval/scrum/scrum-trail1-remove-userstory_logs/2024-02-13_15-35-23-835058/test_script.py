def order_by_points(nums):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    num_tuples = [(num, sum_of_digits(num), index) for index, num in enumerate(nums)]
    num_tuples.sort(key=lambda x: (x[1], x[2]))
    return [t[0] for t in num_tuples]
import unittest

class Test(unittest.TestCase):
    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()