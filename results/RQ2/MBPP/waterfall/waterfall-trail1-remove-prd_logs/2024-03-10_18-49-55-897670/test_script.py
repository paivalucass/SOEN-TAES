def _sum(arr):  
    if not arr:
        return 0
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("Input list must contain only integers")
    return sum(arr)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()