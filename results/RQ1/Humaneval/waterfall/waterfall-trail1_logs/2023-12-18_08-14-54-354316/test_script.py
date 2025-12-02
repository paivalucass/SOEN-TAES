def below_threshold(numbers: list, threshold: int) -> bool:
    for num in numbers:
        if num >= threshold:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_below_threshold_true(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_below_threshold_false(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

if __name__ == '__main__':
    unittest.main()