def add_tuple(test_list, test_tup):
    if not isinstance(test_list, list):
        raise TypeError("The input test_list parameter should be a list")
    if not isinstance(test_tup, tuple):
        raise TypeError("The input test_tup parameter should be a tuple")

    test_list.extend(test_tup)

    return test_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_tuple([5, 6, 7], (9, 10)), [5, 6, 7, 9, 10])

if __name__ == '__main__':
    unittest.main()