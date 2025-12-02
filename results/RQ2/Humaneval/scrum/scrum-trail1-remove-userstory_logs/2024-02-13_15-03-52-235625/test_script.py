def max_element(l: list):
    """
    Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        return "Error: Empty list"
    for element in l:
        if not isinstance(element, (int, float)):
            return "Error: Non-numeric elements"
    return max(l)
import unittest

class TestMaxElement(unittest.TestCase):
    def test_max_element_1(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_max_element_2(self):
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

if __name__ == '__main__':
    unittest.main()