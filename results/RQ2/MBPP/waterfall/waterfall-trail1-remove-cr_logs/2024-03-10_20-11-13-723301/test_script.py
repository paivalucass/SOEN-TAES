def tuple_size(tuple_list):
    '''Write a function to find the size in bytes of the given tuple.'''
    try:
        return sys.getsizeof(tuple_list)
    except TypeError:
        return "Error: Input is not a tuple"
import unittest
import sys

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_size(("A", 1, "B", 2, "C", 3)), sys.getsizeof(("A", 1, "B", 2, "C", 3)))

if __name__ == '__main__':
    unittest.main()