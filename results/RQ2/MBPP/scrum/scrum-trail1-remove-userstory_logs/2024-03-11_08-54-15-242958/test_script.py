def add_lists(test_list: list, test_tup: tuple) -> tuple:
    if not isinstance(test_list, list) or not isinstance(test_tup, tuple):
        raise TypeError("Input parameters must be of type list and tuple respectively")

    new_tup = list(test_tup)
    new_tup.extend(test_list)
    return tuple(new_tup)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_lists([5, 6, 7], (9, 10)), (9, 10, 5, 6, 7))

if __name__ == '__main__':
    unittest.main()