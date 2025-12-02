def common(l1: list, l2: list):
    if not isinstance(l1, list) or not isinstance(l2, list):
        raise TypeError("Inputs must be lists")
    if len(l1) == 0 or len(l2) == 0:
        return []

    common_elements = list(set(l1) & set(l2))

    return sorted(common_elements)
import unittest

class Test(unittest.TestCase):
    def test_common(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

if __name__ == '__main__':
    unittest.main()