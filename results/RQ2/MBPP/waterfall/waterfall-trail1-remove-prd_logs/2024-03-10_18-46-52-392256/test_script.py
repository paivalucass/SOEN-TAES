def rotate_right(lst, m):
    if not lst:
        raise ValueError("Input list is empty")
    
    n = len(lst)
    if m < 0 or m >= n:
        raise ValueError("Value of m is not within the range of the list length")
    
    m = m % n
    rotated_list = lst[-m:] + lst[:-m]
    return rotated_list
import unittest

class Test(unittest.TestCase):
    def test_rotate_right(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [8, 9, 10, 1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()