def common_in_nested_lists(nestedlist):
    if not all(isinstance(sublist, list) for sublist in nestedlist):
        raise ValueError("Input should be a nested list")
    
    common_elements = set(nestedlist[0])
    for sublist in nestedlist[1:]:
        common_elements.intersection_update(sublist)
    
    return list(common_elements) # Convert set to list for output consistency with test cases.
import unittest

class Test(unittest.TestCase):
    def test_common_in_nested_lists(self):
        self.assertEqual(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]), [18, 12])

if __name__ == '__main__':
    unittest.main()