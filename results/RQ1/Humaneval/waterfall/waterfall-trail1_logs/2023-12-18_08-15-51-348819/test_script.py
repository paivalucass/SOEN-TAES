def common(l1: list, l2: list) -> list:
    set_of_list1 = set(l1)
    set_of_list2 = set(l2)
    common_elements = sorted(list(set_of_list1.intersection(set_of_list2)))
    return common_elements
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])

    def test2(self):
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

if __name__ == '__main__':
    unittest.main()