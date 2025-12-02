def sum_squares(lst):
    total_sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            total_sum += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total_sum += lst[i] ** 3
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test2(self):
        self.assertEqual(sum_squares([]), 0)

    def test3(self):
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

if __name__ == '__main__':
    unittest.main()