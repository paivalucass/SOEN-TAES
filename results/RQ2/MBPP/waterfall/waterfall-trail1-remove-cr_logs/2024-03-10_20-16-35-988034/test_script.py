def add_tuple(test_list, test_tup):
    if test_list is None or test_tup is None:
        return test_list
    
    if not isinstance(test_list, list) or not isinstance(test_tup, tuple):
        raise ValueError("Input types should be list and tuple")

    for elem in test_tup:
        test_list.append(elem)
    
    return test_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_tuple([5, 6, 7], (9, 10)), [5, 6, 7, 9, 10])

if __name__ == '__main__':
    unittest.main()