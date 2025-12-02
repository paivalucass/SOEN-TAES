def unique_sublists(list1):
    sublists_count = {}
    for sublist in list1:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in sublists_count:
            sublists_count[tuple_sublist] += 1
        else:
            sublists_count[tuple_sublist] = 1
    return sublists_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()