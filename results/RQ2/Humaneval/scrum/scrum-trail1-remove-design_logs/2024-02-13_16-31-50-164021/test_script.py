def sum_squares(lst):
    sum_total = 0
    for i in range(len(lst)):
        if (i + 1) % 3 == 0:
            sum_total += lst[i] ** 2
        elif (i + 1) % 4 == 0 and (i + 1) % 3 != 0:
            sum_total += lst[i] ** 3
    return sum_total
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_squares([1,2,3]), 6)

    def test2(self):
        self.assertEqual(sum_squares([]), 0)

    def test3(self):
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

if __name__ == '__main__':
    unittest.main()