def unique_sublists(list1):
    if not isinstance(list1, list) or len(list1) == 0:
        return {}

    sublist_count = {}
    
    for sublist in list1:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in sublist_count:
            sublist_count[sublist_tuple] += 1
        else:
            sublist_count[sublist_tuple] = 1

    return sublist_count
import unittest

class Test(unittest.TestCase):
    def test_unique_sublists(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()