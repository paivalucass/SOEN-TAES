def tup_string(input_tuple):
    '''
    This function takes a tuple as input and converts it into a single string.
    It raises a TypeError if the input is not a tuple and a ValueError if any element of the tuple is not a string.
    '''
    if not isinstance(input_tuple, tuple):
        raise TypeError("Input is not a tuple")
    if not all(isinstance(x, str) for x in input_tuple):
        raise ValueError("All elements of the tuple must be strings")
    result = ''.join(input_tuple)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')), "exercises")

if __name__ == '__main__':
    unittest.main()