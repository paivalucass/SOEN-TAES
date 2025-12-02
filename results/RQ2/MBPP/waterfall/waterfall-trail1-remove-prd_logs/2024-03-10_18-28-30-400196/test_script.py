def add_lists(test_list, test_tup):
    if not isinstance(test_list, list) or not isinstance(test_tup, tuple):
        raise TypeError("Input validation: test_list must be a list and test_tup must be a tuple")
    
    result = list(test_tup) + test_list
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_lists([5, 6, 7], (9, 10)), (9, 10, 5, 6, 7))

if __name__ == '__main__':
    unittest.main()