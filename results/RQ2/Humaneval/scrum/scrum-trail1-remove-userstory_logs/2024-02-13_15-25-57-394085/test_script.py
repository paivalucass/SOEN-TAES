def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    import math
    try:
        rounded_lst = [math.ceil(num) for num in lst]
        squared_sum = sum([num**2 for num in rounded_lst])
        return squared_sum
    except TypeError:
        return "Error: Invalid input in the list"
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_squares([1,2,3]), 14)
    
    def test_2(self):
        self.assertEqual(sum_squares([1,4,9]), 98)

    def test_3(self):
        self.assertEqual(sum_squares([1,3,5,7]), 84)

    def test_4(self):
        self.assertEqual(sum_squares([1.4,4.2,0]), 29)

    def test_5(self):
        self.assertEqual(sum_squares([-2.4,1,1]), 6)

if __name__ == '__main__':
    unittest.main()