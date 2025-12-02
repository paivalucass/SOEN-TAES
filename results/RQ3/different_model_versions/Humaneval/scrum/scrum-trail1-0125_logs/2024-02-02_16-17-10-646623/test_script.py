def common(l1: list, l2: list):
    unique_common_elements = sorted(list(set(l1) & set(l2)))
    return unique_common_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

if __name__ == '__main__':
    unittest.main()