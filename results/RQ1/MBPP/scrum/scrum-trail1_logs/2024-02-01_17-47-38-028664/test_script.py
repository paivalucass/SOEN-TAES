def _sum(arr):
    if len(arr) == 0:
        return 0
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Invalid input. Input array should only contain numbers.")
    result = sum(arr)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()