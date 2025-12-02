def tuple_intersection(test_list1, test_list2):
    result = set()
    for tuple1 in test_list1:
        for tuple2 in test_list2:
            if set(tuple1) == set(tuple2):
                result.add(tuple1)
                break
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]), {(4, 5), (3, 4), (5, 6)})

if __name__ == '__main__':
    unittest.main()