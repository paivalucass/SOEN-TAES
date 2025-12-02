def tuple_intersection(test_list1, test_list2):
    intersection = set(test_list1) & set(test_list2)
    return intersection
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]), {(4, 5), (3, 4), (5, 6)})

if __name__ == '__main__':
    unittest.main()