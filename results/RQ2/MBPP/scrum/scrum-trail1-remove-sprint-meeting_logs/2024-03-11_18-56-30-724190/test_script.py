def tuple_size(tuple_list):
    if isinstance(tuple_list, tuple):
        return sys.getsizeof(tuple_list)
    else:
        raise ValueError("Input is not a tuple")
import unittest
import sys

class Test(unittest.TestCase):
    def test_tuple_size(self):
        self.assertEqual(tuple_size(("A", 1, "B", 2, "C", 3)), sys.getsizeof(("A", 1, "B", 2, "C", 3)))

if __name__ == '__main__':
    unittest.main()