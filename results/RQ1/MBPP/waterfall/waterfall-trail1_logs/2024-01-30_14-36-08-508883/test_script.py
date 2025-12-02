def tuple_intersection(test_list1, test_list2):
    set1 = set(test_list1)
    set2 = set(test_list2)
    intersection_set = set1.intersection(set2)
    diff1 = set1.difference(set2)
    diff2 = set2.difference(set1)
    return intersection_set
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]), {(4, 5), (3, 4), (5, 6)})

if __name__ == '__main__':
    unittest.main()