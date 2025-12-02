def sum_squares(lst):
    result = 0
    for i in range(len(lst)):
        if (i + 1) % 3 == 0:
            result += lst[i] ** 2
        elif (i + 1) % 4 == 0 and (i + 1) % 3 != 0:
            result += lst[i] ** 3
    return result
import unittest

class Test(unittest.TestCase):
    def test_sum_squares(self):
        self.assertEqual(sum_squares([1,2,3]), 6)
        self.assertEqual(sum_squares([]), 0)
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

if __name__ == '__main__':
    unittest.main()