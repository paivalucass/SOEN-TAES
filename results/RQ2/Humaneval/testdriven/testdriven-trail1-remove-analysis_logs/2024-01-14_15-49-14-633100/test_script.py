def common(l1: list[int], l2: list[int]) -> list[int]:
    if not l1 or not l2:
        return []

    common_elements = list(set(l1).intersection(l2))
    common_elements.sort()

    return common_elements
import unittest

class Test(unittest.TestCase):
    def test_common(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

if __name__ == '__main__':
    unittest.main()