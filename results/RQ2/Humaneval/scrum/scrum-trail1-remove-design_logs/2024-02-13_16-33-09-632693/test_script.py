def sum_squares(lst):
    return sum([x**2 if i%3==0 else x**3 if i%4==0 else x for i,x in enumerate(lst)])
import unittest

class Test(unittest.TestCase):
    def test_sum_squares(self):
        self.assertEqual(sum_squares([1,2,3]), 6)
        self.assertEqual(sum_squares([]), 0)
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

if __name__ == '__main__':
    unittest.main()