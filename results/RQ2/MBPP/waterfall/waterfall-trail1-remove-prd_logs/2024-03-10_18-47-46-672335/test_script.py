def unique_sublists(input_list):
    sublist_occurrences = {}
    for sublist in input_list:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in sublist_occurrences:
            sublist_occurrences[sublist_tuple] += 1
        else:
            sublist_occurrences[sublist_tuple] = 1
    return sublist_occurrences
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()