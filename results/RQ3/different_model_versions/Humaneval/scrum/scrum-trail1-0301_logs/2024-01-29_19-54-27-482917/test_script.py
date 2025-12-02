def below_threshold(l: list[int], t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    if not isinstance(l, list) or not all(isinstance(num, int) for num in l):
        raise ValueError("Invalid input type. List must contain only integers.")
    if not isinstance(t, int):
        raise ValueError("Invalid input type. Threshold must be an integer.")
        
    return all(num < t for num in l)
import unittest

class TestBelowThreshold(unittest.TestCase):
    def test_all_numbers_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_at_least_one_number_above_threshold(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

if __name__ == '__main__':
    unittest.main()