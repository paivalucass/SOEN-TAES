def tuple_to_dict(test_tup):
    '''
    Write a function to convert the given tuple to a key-value dictionary using adjacent elements. 
    Input: test_tup - the input tuple to be converted to a dictionary
    Output: result_dict - the dictionary created from the input tuple
    '''
    if not isinstance(test_tup, tuple):
        raise ValueError("Input must be a tuple")
    if len(test_tup) % 2 != 0:
        raise ValueError("Input tuple must have an even number of elements")

    result_dict = dict(zip(test_tup[::2], test_tup[1::2]))
    return result_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_dict((1, 5, 7, 10, 13, 5)), {1: 5, 7: 10, 13: 5})

if __name__ == '__main__':
    unittest.main()