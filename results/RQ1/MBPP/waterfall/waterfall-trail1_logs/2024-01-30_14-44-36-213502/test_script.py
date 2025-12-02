def list_tuple(input_list):
    '''Write a function to convert a list to a tuple.'''
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    return tuple(input_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_tuple([5, 10, 7, 4, 15, 3]), (5, 10, 7, 4, 15, 3))

if __name__ == '__main__':
    unittest.main()