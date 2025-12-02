def rotate_right(lst, m):
    if not isinstance(lst, list) or not isinstance(m, int):
        raise TypeError("Input type must be list for 'list' and int for 'm'.")
    if not lst:
        return "Error: Empty input list"
    if m < 0:
        return "Error: Negative value of m"
    m = m % len(lst)
    return lst[-m:] + lst[:-m]
import unittest

class Test(unittest.TestCase):
    def test_rotate_right(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [8, 9, 10, 1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()