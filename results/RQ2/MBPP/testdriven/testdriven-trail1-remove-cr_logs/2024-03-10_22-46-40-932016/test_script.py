import sys

def tuple_size(input_tuple):
    if not isinstance(input_tuple, tuple):
        raise TypeError("Input must be a tuple")

    size_in_bytes = sys.getsizeof(input_tuple)
    return size_in_bytes

import unittest
import sys

class Test(unittest.TestCase):
    def test_tuple_size(self):
        self.assertEqual(tuple_size(("A", 1, "B", 2, "C", 3)), sys.getsizeof(("A", 1, "B", 2, "C", 3)))

if __name__ == '__main__':
    unittest.main()