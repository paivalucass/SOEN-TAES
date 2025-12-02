def sum_squares(lst):
    total_sum = 0
    for index, value in enumerate(lst):
        if index % 3 == 0:
            total_sum += value ** 2
        elif index % 4 == 0 and index % 3 != 0:
            total_sum += value ** 3
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test_sum_squares(self):
        self.assertEqual(sum_squares([1,2,3]), 6)
        self.assertEqual(sum_squares([]), 0)
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

if __name__ == '__main__':
    unittest.main()