def sum_squares(lst):
    def square(num):
        return num ** 2

    def cube(num):
        return num ** 3

    if not all(isinstance(x, int) for x in lst):
        return "Input list must contain only integers."

    total_sum = 0
    for idx, num in enumerate(lst):
        if idx % 3 == 0:
            total_sum += square(num)
        elif idx % 4 == 0 and idx % 3 != 0:
            total_sum += cube(num)
        else:
            total_sum += num

    return total_sum

import unittest

class Test(unittest.TestCase):
    def test_sum_squares(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)
        self.assertEqual(sum_squares([]), 0)
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

if __name__ == '__main__':
    unittest.main()