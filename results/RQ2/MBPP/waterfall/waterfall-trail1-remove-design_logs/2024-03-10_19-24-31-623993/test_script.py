def rotate_right(lst, m):
    if not lst:
        raise ValueError("Input list cannot be empty")

    if m < 0 or m >= len(lst):
        raise ValueError("Value of m must be within the range of the list length")

    m = m % len(lst)
    lst[:] = lst[-m:] + lst[:-m]
    return lst
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [8, 9, 10, 1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()