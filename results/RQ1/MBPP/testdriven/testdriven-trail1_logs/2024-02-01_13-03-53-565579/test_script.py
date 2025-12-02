import sys
def tuple_size(input_tuple):
    '''Write a function to find the size in bytes of the given tuple.'''
    if not isinstance(input_tuple, tuple):
        print("Input parameter is not a tuple")
        return None
    try:
        size = sys.getsizeof(input_tuple)
        return size
    except TypeError:
        print("Error in calculating size")
        return None

# Test cases
assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
assert tuple_size((1, 2, 3, 4, 5, 6)) == sys.getsizeof((1, 2, 3, 4, 5, 6))
assert tuple_size((1,)) == sys.getsizeof((1,))
assert tuple_size("not_a_tuple") is None
assert tuple_size(123) is None
import sys
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_size(("A", 1, "B", 2, "C", 3)), sys.getsizeof(("A", 1, "B", 2, "C", 3)))

if __name__ == '__main__':
    unittest.main()