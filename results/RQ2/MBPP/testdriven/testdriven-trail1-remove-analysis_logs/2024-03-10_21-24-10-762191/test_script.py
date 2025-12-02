def tuple_size(input_tuple):
    import sys
    try:
        return sys.getsizeof(input_tuple)
    except:
        return "Error: Unable to calculate the size of the tuple"
import sys
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_size(("A", 1, "B", 2, "C", 3)), sys.getsizeof(("A", 1, "B", 2, "C", 3)))

if __name__ == '__main__':
    unittest.main()