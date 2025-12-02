def add_lists(input_list, input_tuple):
    '''
    Write a function to append the given list to the given tuples.
    assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
    '''
    
    if not isinstance(input_list, list) or not isinstance(input_tuple, tuple):
        return "Invalid input, please provide a list and a tuple"
    
    return input_tuple + tuple(input_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_lists([5, 6, 7], (9, 10)), (9, 10, 5, 6, 7))

if __name__ == '__main__':
    unittest.main()