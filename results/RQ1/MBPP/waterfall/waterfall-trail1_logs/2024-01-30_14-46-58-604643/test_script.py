import sys

def tuple_size(tuple_list):
    if not isinstance(tuple_list, tuple):
        raise ValueError("Input is not a tuple")
    if len(tuple_list) == 0:
        raise ValueError("Input tuple is empty")

    size = sys.getsizeof(tuple_list)

    return size

assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
assert tuple_size(()) == sys.getsizeof(())
assert tuple_size((1, "hello", [1, 2, 3])) == sys.getsizeof((1, "hello", [1, 2, 3]))
assert tuple_size((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == sys.getsizeof((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
import unittest
import sys

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_size(("A", 1, "B", 2, "C", 3)), sys.getsizeof(("A", 1, "B", 2, "C", 3)))

if __name__ == '__main__':
    unittest.main()