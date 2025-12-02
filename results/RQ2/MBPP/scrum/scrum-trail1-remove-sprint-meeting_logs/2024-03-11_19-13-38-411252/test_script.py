def _sum(arr):
    if not isinstance(arr, list):
        raise TypeError("Input should be a list")

    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Array elements should be numeric")

    result = sum(arr)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()