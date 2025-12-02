def sort_even(l: list) -> list:
    even_indices = l[::2]
    sorted_even_indices = sorted(even_indices)
    result = [0] * len(l)
    result[::2] = sorted_even_indices
    result[1::2] = l[1::2]
    return result

import unittest

class Test(unittest.TestCase):
    def test_sort_even(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

if __name__ == '__main__':
    unittest.main()