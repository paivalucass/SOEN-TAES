def common_in_nested_lists(nestedlist):
    if not isinstance(nestedlist, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(lst, list) and len(lst) > 0 for lst in nestedlist):
        raise ValueError("Input must be a list of non-empty lists")
        
    common_elements = set(nestedlist[0])
    for lst in nestedlist:
        common_elements = common_elements.intersection(lst)
    return list(common_elements)
import unittest

class Test(unittest.TestCase):
    def test_common_in_nested_lists(self):
        self.assertEqual(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]), [18, 12])

if __name__ == '__main__':
    unittest.main()