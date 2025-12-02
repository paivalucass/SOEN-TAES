import math

def sum_squares(lst):
    try:
        if len(lst) == 0:
            return 0
        for num in lst:
            if not isinstance(num, (int, float)):
                return "Error: Non-numeric value in the input list"

        # Round each element in the list to the upper integer (ceiling)
        rounded_lst = [math.ceil(num) for num in lst]

        # Square each rounded element and sum up the squared numbers
        squared_sum = sum([num ** 2 for num in rounded_lst])

        return squared_sum
    except Exception as e:
        return "An error occurred: " + str(e)
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