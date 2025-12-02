def frequency_lists(list1):
    '''Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.'''
    # Input Validation
    if not isinstance(list1, list) or not all(isinstance(item, list) for item in list1) or any(len(item) == 0 for item in list1):
        raise ValueError("Input should be a non-empty list of non-empty lists.")
    
    # Flatten the list of lists
    flattened_list = [item for sublist in list1 for item in sublist]
    
    # Count the frequency of each element
    from collections import Counter
    frequency_dict = dict(Counter(flattened_list))
    
    return frequency_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]), {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1})

if __name__ == '__main__':
    unittest.main()