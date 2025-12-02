def below_threshold(numbers: list[int], threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    :param numbers: List of numbers
    :param threshold: Threshold value
    :return: True if all numbers are below threshold, False otherwise
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for num in numbers:
        if num >= threshold:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

if __name__ == '__main__':
    unittest.main()