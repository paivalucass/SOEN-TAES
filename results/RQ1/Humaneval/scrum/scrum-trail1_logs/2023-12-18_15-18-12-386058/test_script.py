def pluck(arr):
    if not arr:
        return []

    even_values = [i for i in arr if i % 2 == 0]
    if not even_values:
        return []

    min_value = min(even_values)
    min_index = arr.index(min_value)

    return [min_value, min_index]
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(pluck([4,2,3]), [2, 1])

    def test2(self):
        self.assertEqual(pluck([1,2,3]), [2, 1])

    def test3(self):
        self.assertEqual(pluck([]), [])

    def test4(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

if __name__ == '__main__':
    unittest.main()