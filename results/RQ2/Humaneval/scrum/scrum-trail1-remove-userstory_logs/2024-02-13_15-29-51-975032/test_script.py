def double_the_difference(lst):
    if not isinstance(lst, list):
        return 0
    
    result = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            result += num ** 2
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_double_the_difference(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        self.assertEqual(double_the_difference([9, -2]), 81)
        self.assertEqual(double_the_difference([0]), 0)
        self.assertEqual(double_the_difference([]), 0)

if __name__ == '__main__':
    unittest.main()