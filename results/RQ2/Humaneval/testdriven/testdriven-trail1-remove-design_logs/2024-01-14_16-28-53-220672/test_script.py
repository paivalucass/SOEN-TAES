def double_the_difference(lst):
    sum_of_squares_of_odd = 0
    for number in lst:
        if number > 0 and isinstance(number, int) and number % 2 != 0:
            sum_of_squares_of_odd += number ** 2
    return sum_of_squares_of_odd
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        self.assertEqual(double_the_difference([9, -2]), 81)
        self.assertEqual(double_the_difference([0]), 0)
        self.assertEqual(double_the_difference([]), 0)

if __name__ == '__main__':
    unittest.main()