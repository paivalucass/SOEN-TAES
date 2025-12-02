def add_lists(test_list, test_tup):
    if not isinstance(test_list, list) or not isinstance(test_tup, tuple):
        raise TypeError("Inputs should be a list and a tuple")
    return test_tup + tuple(test_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_lists([5, 6, 7], (9, 10)), (9, 10, 5, 6, 7))

if __name__ == '__main__':
    unittest.main()