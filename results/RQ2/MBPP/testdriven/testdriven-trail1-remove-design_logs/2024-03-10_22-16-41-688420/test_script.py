def find_first_occurrence(sorted_array, target):
    if not isinstance(sorted_array, list) or not all(isinstance(i, int) for i in sorted_array):
        return "Error: Input is not a valid list of integers"
    if not isinstance(target, int):
        return "Error: Target is not an integer"
    if len(sorted_array) == 0:
        return -1
    if target not in sorted_array:
        return -1
    return sorted_array.index(target)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()