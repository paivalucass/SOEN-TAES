def sum_squares(lst):
    if not lst:
        return 0
    
    def square_or_cube(num, idx):
        if idx % 3 == 0:
            return num ** 2
        elif idx % 4 == 0 and idx % 3 != 0:
            return num ** 3
        else:
            return num
    
    result = sum(square_or_cube(num, idx) for idx, num in enumerate(lst))
    return result
import unittest

class Test(unittest.TestCase):
    def test_sum_squares(self):
        self.assertEqual(sum_squares([1,2,3]), 6)
        self.assertEqual(sum_squares([]), 0)
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

if __name__ == '__main__':
    unittest.main()