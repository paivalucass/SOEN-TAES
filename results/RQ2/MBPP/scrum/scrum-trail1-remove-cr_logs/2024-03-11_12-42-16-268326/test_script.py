def common_in_nested_lists(nestedlist):
    common_elements = []
    # Write code to find common elements in nested lists
    nested_set = [set(sublist) for sublist in nestedlist]
    common_elements = list(set.intersection(*nested_set))
    return common_elements
import unittest

class Test(unittest.TestCase):
    def test_common_in_nested_lists(self):
        self.assertEqual(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]), [18, 12])

if __name__ == '__main__':
    unittest.main()