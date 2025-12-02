def add_tuple(test_list, test_tup):
    new_list = test_list.copy()
    new_list.extend(test_tup)
    return new_list
import unittest

class Test(unittest.TestCase):
    def test_add_tuple(self):
        self.assertEqual(add_tuple([5, 6, 7], (9, 10)), [5, 6, 7, 9, 10])

if __name__ == '__main__':
    unittest.main()