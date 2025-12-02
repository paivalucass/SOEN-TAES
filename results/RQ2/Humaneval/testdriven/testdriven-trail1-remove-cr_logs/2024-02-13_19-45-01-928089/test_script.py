def median(l: list):
    """Return median of elements in the list l."""
    if not l:
        return "Error: The input list is empty"
    try:
        sorted_list = sorted(l)
        length = len(sorted_list)
        if length % 2 == 0:
            return (sorted_list[length // 2 - 1] + sorted_list[length // 2]) / 2.0
        else:
            return float(sorted_list[length // 2])
    except (TypeError, ValueError):
        return "Error: The input list contains non-numeric elements"
import unittest

class Test(unittest.TestCase):
    def test_median(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

if __name__ == '__main__':
    unittest.main()