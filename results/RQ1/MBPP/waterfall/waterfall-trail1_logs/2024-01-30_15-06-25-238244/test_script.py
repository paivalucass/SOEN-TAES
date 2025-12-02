def unique_sublists(list1):
    unique_sublists = {}
    for sublist in list1:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in unique_sublists:
            unique_sublists[tuple_sublist] += 1
        else:
            unique_sublists[tuple_sublist] = 1
    return unique_sublists
import unittest

class Test(unittest.TestCase):
    def test_unique_sublists(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()