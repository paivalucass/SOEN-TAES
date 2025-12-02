def max_element(l: list) -> int:
    if not isinstance(l, list):
        raise TypeError("Input parameter must be a list")

    if len(l) == 0:
        return None
    else:
        return max(l)
import unittest

class Test(unittest.TestCase):
    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

if __name__ == '__main__':
    unittest.main()