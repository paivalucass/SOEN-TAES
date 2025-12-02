def all_unique(test_list):
    '''
    Write a python function to check if the elements of a given list are unique or not.
    assert all_unique([1,2,3]) == True
    '''
    if not isinstance(test_list, list):
        raise TypeError("Input must be a list")
    
    if any(isinstance(elem, (list, dict)) for elem in test_list):
        raise ValueError("Input list contains non-hashable elements")
    
    unique_set = set(test_list)
    
    return len(test_list) == len(unique_set)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_unique([1,2,3]), True)

if __name__ == '__main__':
    unittest.main()