def unique_sublists(list1):
    from collections import defaultdict
    result_dict = defaultdict(int)
    for sublist in list1:
        sublist_tuple = tuple(sublist)
        result_dict[sublist_tuple] += 1
    return dict(result_dict)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] ), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()