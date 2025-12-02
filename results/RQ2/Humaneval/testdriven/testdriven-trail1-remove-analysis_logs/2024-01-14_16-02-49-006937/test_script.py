def pluck(arr):
    if not arr:
        return []

    even_values = [x for x in arr if x % 2 == 0]
    if not even_values:
        return []

    min_even = min(even_values)
    min_even_indices = [i for i, x in enumerate(arr) if x == min_even]
    min_even_index = min(min_even_indices)

    return [min_even, min_even_index]
import unittest

class Test(unittest.TestCase):
    def test_pluck(self):
        self.assertEqual(pluck([4,2,3]), [2, 1])
        self.assertEqual(pluck([1,2,3]), [2, 1])
        self.assertEqual(pluck([]), [])
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

if __name__ == '__main__':
    unittest.main()