def add_tuple(test_list, test_tup):
    if not isinstance(test_list, list):
        raise TypeError('First argument must be a list')
    if not isinstance(test_tup, tuple):
        raise TypeError('Second argument must be a tuple')
    new_list = test_list.copy()
    new_list.extend(test_tup)
    return new_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_tuple([5, 6, 7], (9, 10)), [5, 6, 7, 9, 10])

if __name__ == '__main__':
    unittest.main()