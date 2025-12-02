def tuple_intersection(test_list1, test_list2):
    if not isinstance(test_list1, list) or not isinstance(test_list2, list):
        return "Input lists must be of type list"
    if len(test_list1) == 0 or len(test_list2) == 0:
        return "Input lists cannot be empty"

    result = set(test_list1).intersection(test_list2)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]), {(4, 5), (3, 4), (5, 6)})

if __name__ == '__main__':
    unittest.main()