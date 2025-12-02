def add_lists(test_list, test_tup):
    return tuple(list(test_tup) + test_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_lists([5, 6, 7], (9, 10)), (9, 10, 5, 6, 7))

if __name__ == '__main__':
    unittest.main()