def add_tuple(test_list, test_tup):
    if not isinstance(test_list, list) or not isinstance(test_tup, tuple):
        raise TypeError("Invalid input types. test_list must be a list and test_tup must be a tuple.")

    updated_list = test_list + list(test_tup)
    return updated_list
import unittest

class Test(unittest.TestCase):
    def test_add_tuple(self):
        self.assertEqual(add_tuple([5, 6, 7], (9, 10)), [5, 6, 7, 9, 10])

if __name__ == '__main__':
    unittest.main()