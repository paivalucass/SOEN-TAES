def sum_squares(lst):
    result = 0
    for index, value in enumerate(lst):
        if index % 3 == 0:
            result += value ** 2
        elif index % 4 == 0 and index % 3 != 0:
            result += value ** 3
        else:
            result += value
    return result
import unittest

class Test(unittest.TestCase):
    def test_sum_squares(self):
        self.assertEqual(sum_squares([1,2,3]), 6)
        self.assertEqual(sum_squares([]), 0)
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

if __name__ == '__main__':
    unittest.main()