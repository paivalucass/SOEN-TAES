def add_lists(input_list, input_tuple):
    if isinstance(input_list, list) and isinstance(input_tuple, tuple):
        return input_tuple + tuple(input_list)
    else:
        return "Invalid input type"
import unittest

class Test(unittest.TestCase):
    def test_add_lists(self):
        self.assertEqual(add_lists([5, 6, 7], (9, 10)), (9, 10, 5, 6, 7))

if __name__ == '__main__':
    unittest.main()