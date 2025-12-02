import math

def sum_squares(lst):
    if not isinstance(lst, list) or not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input parameter 'lst' must be a list of floating-point numbers")

    if len(lst) == 0:
        raise ValueError("Input list cannot be empty")

    rounded_squares_sum = sum([math.ceil(x)**2 for x in lst])
    return rounded_squares_sum
import math

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(function_under_test([1,2,3]), 14)

    def test_2(self):
        self.assertEqual(function_under_test([1,4,9]), 98)

    def test_3(self):
        self.assertEqual(function_under_test([1,3,5,7]), 84)

    def test_4(self):
        self.assertEqual(function_under_test([1.4,4.2,0]), 29)

    def test_5(self):
        self.assertEqual(function_under_test([-2.4,1,1]), 6)

if __name__ == '__main__':
    unittest.main()