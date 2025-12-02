def add_dict_to_tuple(test_tup, test_dict):
    '''Write a function to add a dictionary to the tuple. The output should be a tuple.
    Parameters:
    test_tup (tuple): Input tuple
    test_dict (dict): Input dictionary
    Returns:
    tuple: Output tuple with dictionary added at the end
    Raises:
    ValueError: If input tuple is empty or input dictionary is empty
    TypeError: If input tuple contains elements other than integers
    TypeError: If input dictionary contains keys other than strings or values other than integers
    '''
    # Check if input tuple is empty
    if len(test_tup) == 0:
        raise ValueError("Input tuple is empty")
    
    # Check if input dictionary is empty
    if len(test_dict) == 0:
        raise ValueError("Input dictionary is empty")
    
    # Check if input tuple contains elements other than integers
    if not all(isinstance(x, int) for x in test_tup):
        raise TypeError("Input tuple contains elements other than integers")
    
    # Check if input dictionary contains keys other than strings or values other than integers
    if not all(isinstance(k, str) and isinstance(v, int) for k, v in test_dict.items()):
        raise TypeError("Input dictionary contains keys other than strings or values other than integers")
    
    # Add dictionary to the tuple and return the updated tuple
    return test_tup + (test_dict,)

assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})

import unittest

class Test(unittest.TestCase):
    def test_add_dict_to_tuple(self):
        self.assertEqual(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3}), (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3}))

if __name__ == '__main__':
    unittest.main()