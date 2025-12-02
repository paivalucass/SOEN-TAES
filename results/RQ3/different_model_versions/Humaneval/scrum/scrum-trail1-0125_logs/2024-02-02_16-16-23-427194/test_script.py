def below_threshold(l: list, t: int):
    if not isinstance(l, list) or not all(isinstance(num, (int, float)) for num in l):
        raise TypeError("Input list l must be a list of numbers")
    
    if not isinstance(t, int):
        raise TypeError("Input threshold t must be an integer")
    
    return all(num < t for num in l) if l else True
import unittest

class Test(unittest.TestCase):
    def test_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

if __name__ == '__main__':
    unittest.main()