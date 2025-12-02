def pluck(arr):
    even_values = [x for x in arr if x % 2 == 0]
    if not even_values:
        return []
    smallest_even_value = min(even_values)
    smallest_even_index = arr.index(smallest_even_value)
    return [smallest_even_value, smallest_even_index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pluck([4,2,3]), [2, 1])
        self.assertEqual(pluck([1,2,3]), [2, 1])
        self.assertEqual(pluck([]), [])
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

if __name__ == '__main__':
    unittest.main()