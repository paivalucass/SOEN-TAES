def rotate_right(lst, m):
    if len(lst) == 0:
        return lst
    n = len(lst)
    m = m % n
    lst[:] = lst[-m:] + lst[:-m]
    return lst
import unittest

class Test(unittest.TestCase):
    def test_rotate_right(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [8, 9, 10, 1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()