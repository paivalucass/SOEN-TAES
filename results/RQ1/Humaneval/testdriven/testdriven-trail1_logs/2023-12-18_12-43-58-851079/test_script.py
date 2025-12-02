def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def ignore_negative_non_integer(lst):
    return [x for x in lst if isinstance(x, int) and x >= 0]

def sum_of_squares(lst):
    return sum(x**2 for x in lst)

def double_the_difference(lst):
    filter_result = filter_odd_numbers(lst)
    ignore_result = ignore_negative_non_integer(filter_result)
    sum_result = sum_of_squares(ignore_result)
    return sum_result

# Test cases
print(double_the_difference([1, 3, 2, 0]))  # Expected output: 10
print(double_the_difference([-1, -2, 0]))  # Expected output: 0
print(double_the_difference([9, -2]))  # Expected output: 81
print(double_the_difference([0]))  # Expected output: 0
import unittest

class Test(unittest.TestCase):
    def test_double_the_difference(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        self.assertEqual(double_the_difference([9, -2]), 81)
        self.assertEqual(double_the_difference([0]), 0)
        self.assertEqual(double_the_difference([]), 0)

if __name__ == '__main__':
    unittest.main()