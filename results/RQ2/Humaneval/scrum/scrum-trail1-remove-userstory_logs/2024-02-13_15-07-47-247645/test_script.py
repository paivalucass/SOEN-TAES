def below_threshold(l: list, t: int):
    if not isinstance(t, int):
        raise ValueError("Threshold must be an integer")
    if len(l) == 0:
        raise ValueError("Input list cannot be empty")
    
    for num in l:
        if num >= t:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_below_threshold_true(self):
        self.assertEqual(below_threshold([1, 2, 4, 10], 100), True)

    def test_below_threshold_false(self):
        self.assertEqual(below_threshold([1, 20, 4, 10], 5), False)

if __name__ == '__main__':
    unittest.main()