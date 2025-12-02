def sum_squares(lst):
    squared_sum = sum([int(x)**2 for x in lst])
    return squared_sum
import unittest

class Test(unittest.TestCase):
    def test_sum_squares(self):
        self.assertEqual(sum_squares([1,2,3]), 14)
        self.assertEqual(sum_squares([1,4,9]), 98)
        self.assertEqual(sum_squares([1,3,5,7]), 84)
        self.assertEqual(sum_squares([1.4,4.2,0]), 29)
        self.assertEqual(sum_squares([-2.4,1,1]), 6)

if __name__ == '__main__':
    unittest.main()