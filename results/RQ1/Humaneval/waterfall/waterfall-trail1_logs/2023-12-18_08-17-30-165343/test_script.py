def pluck(arr):
    even_values = [x for x in arr if x % 2 == 0]
    if len(even_values) == 0:
        return []

    min_value = min(even_values)
    min_index = arr.index(min_value)
    return [min_value, min_index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pluck([4,2,3]), [2, 1])
        self.assertEqual(pluck([1,2,3]), [2, 1])
        self.assertEqual(pluck([]), [])
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

if __name__ == '__main__':
    unittest.main()