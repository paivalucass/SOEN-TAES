def tuple_intersection(test_list1, test_list2):
    if not isinstance(test_list1, list) or not isinstance(test_list2, list):
        return set()

    set1 = set([tuple(sorted(x)) for x in test_list1])
    set2 = set([tuple(sorted(x)) for x in test_list2])

    return set1 & set2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]), {(3, 4), (5, 6), (4, 5)})

if __name__ == '__main__':
    unittest.main()