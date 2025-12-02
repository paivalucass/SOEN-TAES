def below_threshold(l: list, t: int):
    if not isinstance(l, list) or not all(isinstance(i, (int, float)) for i in l):
        raise TypeError("Input data must be a list of numbers")
    if not isinstance(t, (int, float)):
        raise TypeError("Threshold must be a number")

    if not l:
        return True  # Empty list is always below threshold

    for num in l:
        if num >= t:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_below_threshold(self):
        self.assertEqual(below_threshold([1, 2, 4, 10], 100), True)
        self.assertEqual(below_threshold([1, 20, 4, 10], 5), False)

if __name__ == '__main__':
    unittest.main()
