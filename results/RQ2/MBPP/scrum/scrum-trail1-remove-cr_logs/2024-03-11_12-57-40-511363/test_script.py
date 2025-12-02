def count_X(tup, x):
    if not isinstance(tup, tuple):
        raise ValueError("Input is not a tuple")
    if not isinstance(x, (int, float, complex, str)):
        raise ValueError("Element is not of the correct type")
    
    return tup.count(x)
import unittest

class Test(unittest.TestCase):
    def test_count_X(self):
        self.assertEqual(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4), 0)

if __name__ == '__main__':
    unittest.main()