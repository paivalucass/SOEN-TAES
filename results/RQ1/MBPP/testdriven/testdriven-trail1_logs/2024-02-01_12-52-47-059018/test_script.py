def tuple_intersection(test_list1, test_list2):
    if not all(isinstance(item, tuple) for item in test_list1) or not all(isinstance(item, tuple) for item in test_list2):
        raise ValueError("Input parameters must be tuple lists")

    intersection_set = set(test_list1).intersection(test_list2)

    return intersection_set
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]), {(4, 5), (3, 4), (5, 6)})

if __name__ == '__main__':
    unittest.main()