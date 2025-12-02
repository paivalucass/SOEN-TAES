def common(l1: list, l2: list) -> list:
    common = []
    for i in l1:
        if i in l2 and i not in common:
            common.append(i)
    return sorted(common)
import unittest

class TestCommon(unittest.TestCase):
    def test_common(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

if __name__ == '__main__':
    unittest.main()