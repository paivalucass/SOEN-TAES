def replace_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "Error: Input should be lists"
    
    if len(list1) == 0 or len(list2) == 0:
        return "Error: Input lists cannot be empty"
    
    if len(list1) < 1:
        return list2
    
    modified_list1 = list1[:-1] + list2
    return modified_list1
import unittest

class Test(unittest.TestCase):
    def test_replace_list(self):
        self.assertEqual(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]), [1, 3, 5, 7, 9, 2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()