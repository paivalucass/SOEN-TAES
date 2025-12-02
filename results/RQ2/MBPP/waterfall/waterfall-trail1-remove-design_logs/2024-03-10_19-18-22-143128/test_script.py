def tuple_intersection(test_list1, test_list2):
    if not isinstance(test_list1, list) or not isinstance(test_list2, list):
        raise ValueError("Input parameters must be lists")

    if not test_list1 or not test_list2:
        return []

    set1 = set(test_list1)
    set2 = set(test_list2)
    intersection_result = set1.intersection(set2)
    result = []
    for item in intersection_result:
        if item in test_list1 and item in test_list2:
            result.append(item)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]), {(4, 5), (3, 4), (5, 6)})

if __name__ == '__main__':
    unittest.main()