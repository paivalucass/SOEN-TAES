def common_in_nested_lists(nestedlist):
    try:
        if not all(isinstance(i, list) for i in nestedlist):
            raise ValueError("Input is not a list of nested lists")
        
        common_elements = set(nestedlist[0])
        for lst in nestedlist[1:]:
            common_elements = common_elements.intersection(set(lst))
        
        return sorted(list(common_elements))
        
    except ValueError:
        return "Error: Invalid input data"
import unittest

class Test(unittest.TestCase):
    def test_common_in_nested_lists(self):
        self.assertEqual(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]), [12, 18])

if __name__ == '__main__':
    unittest.main()