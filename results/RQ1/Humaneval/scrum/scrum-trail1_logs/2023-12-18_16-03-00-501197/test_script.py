def double_the_difference(lst):
    if not all(isinstance(x, (int, float)) for x in lst):
        return "Input list should contain only numbers"
    
    odd_squares_sum = 0
    
    for num in lst:
        if num % 2 != 0 and num > 0:
            odd_squares_sum += num ** 2
    
    return odd_squares_sum
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