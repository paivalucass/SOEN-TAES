def rotate_right(input_list, num_rotations):
    if not isinstance(input_list, list) or not isinstance(num_rotations, int) or num_rotations < 0:
        raise ValueError("Input list must be a non-empty list and number of rotations must be a non-negative integer.")

    if len(input_list) == 0:
        return []

    num_rotations = num_rotations % len(input_list)
    return input_list[-num_rotations:] + input_list[:-num_rotations] 
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [8, 9, 10, 1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()