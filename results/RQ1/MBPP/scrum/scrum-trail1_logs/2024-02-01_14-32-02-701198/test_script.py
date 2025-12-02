def add_lists(test_list, test_tup):
    if not test_list or not test_tup:
        raise ValueError("Input list and tuple cannot be empty")

    if not isinstance(test_list, list) or not isinstance(test_tup, tuple):
        raise TypeError("Input list should be a list and input tuple should be a tuple")

    new_tuple = test_tup + tuple(test_list)
    return new_tuple
import unittest

class Test(unittest.TestCase):
    def test_add_lists(self):
        self.assertEqual(add_lists([5, 6, 7], (9, 10)), (9, 10, 5, 6, 7))

if __name__ == '__main__':
    unittest.main()