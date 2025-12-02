def sort_even(l: list) -> list:
    even_indices = l[::2]
    even_indices.sort()
    result = l.copy()
    result[::2] = even_indices
    return result
import unittest

class Test(unittest.TestCase):
    def test_sort_even(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

if __name__ == '__main__':
    unittest.main()