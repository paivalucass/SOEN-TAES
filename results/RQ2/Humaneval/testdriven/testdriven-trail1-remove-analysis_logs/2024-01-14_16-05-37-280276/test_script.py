def order_by_points(nums):
    def calculate_digit_sum(num):
        return sum(int(digit) for digit in str(abs(num)))

    if not all(isinstance(num, int) for num in nums):
        raise ValueError("Input list contains non-integer elements")

    tuple_list = [(num, calculate_digit_sum(num), index) for index, num in enumerate(nums)]

    sorted_list = [tup[0] for tup in sorted(tuple_list, key=lambda x: (x[1], x[2]))]

    return sorted_list

import unittest

class Test(unittest.TestCase):
    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()