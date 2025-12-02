def tuple_size(tuple_list):
    return sys.getsizeof(tuple_list)
import sys
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_size(("A", 1, "B", 2, "C", 3)), sys.getsizeof(("A", 1, "B", 2, "C", 3)))

if __name__ == '__main__':
    unittest.main()