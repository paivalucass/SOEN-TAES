def add_tuple(test_list, test_tup):
    return test_list + list(test_tup)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_tuple([5, 6, 7], (9, 10)), [5, 6, 7, 9, 10])

if __name__ == '__main__':
    unittest.main()