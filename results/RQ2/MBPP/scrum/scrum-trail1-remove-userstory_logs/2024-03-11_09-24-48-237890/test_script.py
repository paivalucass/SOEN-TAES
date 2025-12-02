def rotate_right(lst, num_rotations):
    if not lst:
        raise ValueError("Input list cannot be empty")
    
    n = len(lst)
    num_rotations = num_rotations % n
    
    if num_rotations < 0:
        num_rotations += n
    
    result = lst[n - num_rotations:] + lst[:n - num_rotations]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_rotate_right(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [8, 9, 10, 1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()