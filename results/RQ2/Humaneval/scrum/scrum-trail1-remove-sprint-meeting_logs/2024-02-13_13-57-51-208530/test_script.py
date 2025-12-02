def common(l1: list, l2: list) -> list:
    if not isinstance(l1, list) or not isinstance(l2, list):
        raise ValueError("Both inputs must be lists")
    if len(l1) == 0 or len(l2) == 0:
        raise ValueError("Input lists must contain elements")

    common_elements = list(set(l1) & set(l2))
    common_elements.sort()

    return common_elements
import unittest

class Test(unittest.TestCase):
    def test_common_elements(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

if __name__ == '__main__':
    unittest.main()