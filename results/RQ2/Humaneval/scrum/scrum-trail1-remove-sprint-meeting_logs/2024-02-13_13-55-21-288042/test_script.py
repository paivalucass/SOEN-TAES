def below_threshold(l: list, t: int) -> bool:
    if not l or t < 0:
        return False
    return all(num < t for num in l)
import unittest

class Test(unittest.TestCase):
    def test_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

if __name__ == '__main__':
    unittest.main()