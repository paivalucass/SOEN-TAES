def common_in_nested_lists(nestedlist):
    common_elements = set(nestedlist[0])
    for lst in nestedlist[1:]:
        common_elements.intersection_update(lst)
    return list(common_elements)
import unittest

class Test(unittest.TestCase):
    def test_common_in_nested_lists(self):
        self.assertEqual(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]), [18, 12])

if __name__ == '__main__':
    unittest.main()