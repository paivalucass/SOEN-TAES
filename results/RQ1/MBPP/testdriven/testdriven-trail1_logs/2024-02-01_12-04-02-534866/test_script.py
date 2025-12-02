def common_in_nested_lists(nestedlist):
    '''
    Write a function to find the common elements in given nested lists.
    assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
    '''
    if not nestedlist or any(not sublist for sublist in nestedlist):
        return []

    if not all(isinstance(sublist, list) for sublist in nestedlist):
        raise ValueError("Input must be a valid nested list")

    common_elements = set(nestedlist[0])
    for lst in nestedlist[1:]:
        common_elements = common_elements.intersection(lst)
    
    return list(common_elements)
import unittest

class Test(unittest.TestCase):
    def test_common_in_nested_lists(self):
        self.assertEqual(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]), [18, 12])

if __name__ == '__main__':
    unittest.main()