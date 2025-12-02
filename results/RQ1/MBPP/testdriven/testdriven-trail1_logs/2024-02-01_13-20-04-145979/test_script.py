def rotate_right(input_list, rotation_count):
    if len(input_list) == 0 or rotation_count < 0:
        return input_list
    rotation_count = rotation_count % len(input_list)
    return input_list[-rotation_count:] + input_list[:-rotation_count]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [8, 9, 10, 1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()