def sum_squares(lst):
    if not lst:
        return 0
    
    result = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            result += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += lst[i] ** 3
        else:
            result += lst[i]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_2(self):
        self.assertEqual(sum_squares([]), 0)

    def test_3(self):
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

if __name__ == '__main__':
    unittest.main()