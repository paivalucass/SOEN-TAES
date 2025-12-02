def pluck(arr):
    even_values = [num for num in arr if num % 2 == 0]
    if not even_values:
        return []

    min_even = min(even_values)
    min_even_index = arr.index(min_even)

    return [min_even, min_even_index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pluck([4,2,3]), [2, 1])

if __name__ == '__main__':
    unittest.main()