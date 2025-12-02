def add_lists(test_list, test_tup):
    if isinstance(test_list, list) and isinstance(test_tup, tuple):
        return test_tup + tuple(test_list)
    else:
        return "Invalid input types"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_lists([5, 6, 7], (9, 10)), (9, 10, 5, 6, 7))

if __name__ == '__main__':
    unittest.main()