def solution(lst):
    sum_of_odd_elements = sum(lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0)
    return sum_of_odd_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([5, 8, 7, 1]), 12)
        self.assertEqual(function_under_test([3, 3, 3, 3, 3]), 9)
        self.assertEqual(function_under_test([30, 13, 24, 321]), 0)

if __name__ == '__main__':
    unittest.main()