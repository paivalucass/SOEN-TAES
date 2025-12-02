def median(l: list):
    """Return median of elements in the list l."""
    sorted_list = sorted(l)
    length = len(sorted_list)
    if length % 2 == 0:
        return (sorted_list[length//2 - 1] + sorted_list[length//2]) / 2
    else:
        return sorted_list[length//2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

if __name__ == '__main__':
    unittest.main()